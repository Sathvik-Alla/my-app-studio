# Conversation evidence

AI-drafted task summary, not a transcript or grade. It may be public. Use actual
short words or labeled paraphrases; disclose help and leave missing responses
pending. The learner reviews, corrects or removes new excerpts before commit/push.
Accuracy approval is not proof of understanding. Label simulated trials explicitly.

**Available conversation context:** This Studio 2 chat, from local setup through the APP-003 keep decision.

## APP-001

- Prediction: (learner paraphrase) First-time visitors will find their preferred category more quickly because the three categories are clearly displayed.
- Check interpretation: (learner paraphrase) The test would catch a homepage that still displays “Your Project” after the brand file is updated. It checks that the homepage loads and returns the correct Animated Realms branding and headline.
- Browser observation: (learner paraphrase) In Chrome, the learner saw the compass logo, blue background, large headline, and Anime, Cartoons, and Comics cards. The layout looked organized and matched the branding they wanted. The starter preview had looked generic and displayed “Your Project.”
  - Follow-up (learner's words): “The three categories are easy to identify, and the navigation helps visitors reach the section they want without searching through the entire page.”
- Keep decision: (learner paraphrase) Keep the design because visitors can clearly identify the three categories and navigate to the content they are interested in.
- Review: The learner reviewed and approved the prediction, test interpretation, browser observation, keep decision, and AI assistance summary. The learner confirmed the follow-up quote accurately describes their Chrome experience and approved including it in the APP-001 pull request.
- Help/gaps: AI located the IS117 site and suggested the Explorer archetype and homepage promise. The learner adopted both, said the promise helps visitors understand the site's purpose, and approved the implementation plan. AI built the homepage, verified category navigation in Chromium, and shared the homepage contract result. The Windows symbolic-link test passed on rerun as part of the full APP-001 check.
- Evidence links / next step: [APP-001 issue](https://github.com/Sathvik-Alla/my-app-studio/issues/1) and [homepage contract](contracts/test_homepage.py). Review the APP-001 pull request and its CI results.

## APP-002

- Prediction: (learner paraphrase) Opening `/dashboard` without logging in should redirect to the login page without showing private dashboard information. After a successful login, the dashboard should open. After logout, access should end.
- Check interpretation: (learner paraphrase) If logout only cleared the browser cookie, someone with a copy could still access private account information. The HTTP 401 response confirms that the server rejected the copied session cookie after logout.
- Browser observation: (learner paraphrase) In Chrome, the Animated Realms homepage remained public. The signup form required a password of at least 15 characters. After logging in, the learner reached their private member dashboard. After logging out and reopening `/dashboard`, they were redirected to login without seeing private information. The learner concluded that dashboard access requires authentication and ends at logout.
- Keep decision: (learner paraphrase) Keep the current flow because it worked as expected and was easy to use. The homepage stayed public, visitors could sign up, and members could access their private dashboard after login. Reopening the dashboard after logout redirected to login without showing private information. The learner also felt the 15-character minimum encourages stronger passwords.
- Review: The learner reviewed and approved all five APP-002 entries.
- Help/gaps: AI proposed keeping the homepage public and adding member signup, login, a private dashboard, and logout. The learner agreed, supplied the dashboard prediction, and approved the plan. AI connected the forms and API to the prepared security helpers, ran the full cumulative checks, and shared the session replay result.
- Evidence links / next step: [APP-002 issue](https://github.com/Sathvik-Alla/my-app-studio/issues/4) and [account contracts](contracts/test_accounts.py). Review the APP-002 PR and CI results.

## APP-003

- Prediction: (learner paraphrase) A logged-in member who directly requests `GET /api/admin` should get HTTP 403 Forbidden because they are authenticated and lack administrator permissions. A signed-out visitor should get HTTP 401 Unauthorized. Members should still reach their private dashboard. The learner expects the direct request test to catch an app that checks login but skips the administrator role check.
- Check interpretation: (learner paraphrase) The same session received HTTP 200 after promotion and HTTP 403 after downgrade without another login. This shows that protected requests use the current database role. The test would catch a session retaining administrator privileges after the user's role was downgraded.
- Browser observation: (learner paraphrase) In Chrome, opening `/admin` as a signed-in member showed “Admin access required.” After promotion through the trusted CLI in Git Bash, refreshing `/admin` in the same session showed “Administration” and welcomed the administrator account. After downgrade to member through the CLI, another refresh showed “Admin access required” again.
- Keep decision: (learner paraphrase) Keep the implementation because it prevents members from accessing administrator-only information and removes administrator privileges on the first protected request after a downgrade.
- Review: The learner reviewed and approved all five APP-003 entries.
- Help/gaps: AI prompted the direct API prediction, implemented the approved role checks using the prepared helper, ran the full cumulative checks, shared the same-session Chromium result, and provided the CLI steps for the learner's Chrome test.
- Evidence links / next step: [APP-003 issue](https://github.com/Sathvik-Alla/my-app-studio/issues/6) and [role contracts](contracts/test_roles.py). Review the APP-003 pull request and CI results.
