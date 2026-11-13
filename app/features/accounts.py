"""Browser and JSON account routes backed by the prepared session helpers."""

import re
from typing import Annotated
from urllib.parse import parse_qsl

from fastapi import APIRouter, Depends, Header, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()


def check_api_csrf(
    request: Request, x_csrf_token: Annotated[str | None, Header()] = None
):
    """Validate the token from the same-origin API client."""
    security.require_csrf(request, x_csrf_token)


API_CSRF = Depends(check_api_csrf)
CurrentUser = Annotated[dict[str, str], Depends(security.require_user)]


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Provide the session's CSRF token to an API client."""
    return {"csrf_token": security.csrf_token(request, response)}


def register(request: Request, credentials: SignupInput):
    """Share the signup throttle and member creation across both interfaces."""
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


@router.post(
    "/api/signup", status_code=201, response_model=PublicUser, dependencies=[API_CSRF]
)
def api_signup(request: Request, credentials: SignupInput):
    """Create a member account."""
    return register(request, credentials)


@router.post("/api/login", response_model=PublicUser, dependencies=[API_CSRF])
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Start an authenticated session."""
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me", response_model=PublicUser)
def api_me(user: CurrentUser):
    """Return only the public fields of the authenticated user."""
    return user


@router.post("/api/logout", dependencies=[API_CSRF])
def api_logout(request: Request, response: Response, _user: CurrentUser):
    """Revoke the authenticated session."""
    security.logout(request, response)
    return {"status": "ok"}


async def read_form(request: Request) -> dict[str, str]:
    """Read a small URL-encoded form and reject ambiguous duplicate fields."""
    media_type = (
        request.headers.get("content-type", "").partition(";")[0].strip().lower()
    )
    if media_type != "application/x-www-form-urlencoded":
        raise HTTPException(415, "Submit this request using the account form.")
    body = bytearray()
    async for chunk in request.stream():
        if len(body) + len(chunk) > 8192:
            raise HTTPException(413, "This form is too large.")
        body.extend(chunk)
    try:
        pairs = parse_qsl(
            body.decode("ascii"),
            keep_blank_values=True,
            max_num_fields=4,
            errors="strict",
        )
    except ValueError as error:
        raise HTTPException(422, "This form could not be read.") from error
    fields = dict(pairs)
    if len(fields) != len(pairs):
        raise HTTPException(422, "Submit each form field once.")
    return fields


AccountForm = Annotated[dict[str, str], Depends(read_form)]


def account_page(request, action, *, error=None, username=""):
    """Render an account form with safe fields and an optional error."""
    context = {
        "action": action,
        "username": username,
        "error": error.detail if error else None,
    }
    return csrf_page(request, "account.html", context, error)


def csrf_page(request, template, context, error=None):
    """Render a form and carry over any new session cookie."""
    response = Response(headers=error.headers if error else None)
    context["csrf_token"] = security.csrf_token(request, response)
    page = request.app.state.templates.TemplateResponse(
        request=request,
        name=template,
        context=context,
        status_code=error.status_code if error else 200,
        headers=error.headers if error else None,
    )
    page.raw_headers.extend(
        header for header in response.raw_headers if header[0] == b"set-cookie"
    )
    return page


def redirect(path):
    """Navigate with a GET after form submission."""
    return RedirectResponse(path, status_code=303)


@router.get("/signup", include_in_schema=False)
def signup_page(request: Request):
    """Show the signup form."""
    return account_page(request, "signup")


@router.get("/login", include_in_schema=False)
def login_page(request: Request):
    """Show the login form."""
    return account_page(request, "login")


def submit_account(request, fields, action):
    """Validate browser credentials and run the selected account action."""
    is_signup = action == "signup"
    token = fields.pop("csrf_token", None)
    username = ""
    try:
        security.require_csrf(request, token)
        candidate = fields.get("username", "").strip().lower()
        if re.fullmatch(r"[a-z0-9_]{3,32}", candidate):
            username = candidate
        if is_signup:
            register(request, SignupInput.model_validate(fields))
            return redirect("/login")
        credentials = LoginInput.model_validate(fields)
        response = redirect("/dashboard")
        security.login(request, response, credentials.username, credentials.password)
        return response
    except ValidationError:
        error = HTTPException(422, "Check the username and password requirements.")
    except HTTPException as failure:
        error = failure
    return account_page(request, action, error=error, username=username)


@router.post("/signup", include_in_schema=False)
def signup_form(request: Request, fields: AccountForm):
    """Create a member and direct them to login."""
    return submit_account(request, fields, "signup")


@router.post("/login", include_in_schema=False)
def login_form(request: Request, fields: AccountForm):
    """Sign in and redirect to the dashboard."""
    return submit_account(request, fields, "login")


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """Render the private dashboard only for a live authenticated session."""
    user = security.authenticate(request)
    if user is None:
        return redirect("/login")
    return csrf_page(request, "dashboard.html", {"member": user})


@router.post("/logout", include_in_schema=False)
def logout_form(request: Request, fields: AccountForm):
    """Revoke a browser session and return to the public homepage."""
    security.require_csrf(request, fields.get("csrf_token"))
    response = redirect("/")
    security.logout(request, response)
    return response
