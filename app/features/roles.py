"""Protect administrator resources using the current server-side role."""

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from app.security import require_admin

router = APIRouter()


@router.get("/api/admin", dependencies=[Depends(require_admin)])
def admin_api():
    """Return the protected administration response."""
    return {"message": "Welcome to Animated Realms administration."}


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """Render administration only after checking the current account role."""
    templates = request.app.state.templates
    try:
        admin = require_admin(request)
    except HTTPException as error:
        if error.status_code == 401:
            return RedirectResponse("/login", status_code=303)
        if error.status_code != 403:
            raise
        return templates.TemplateResponse(
            request=request, name="admin.html", context={}, status_code=403
        )
    return templates.TemplateResponse(
        request=request, name="admin.html", context={"admin": admin}
    )
