from typing import Optional
from fastapi import Depends, Request, APIRouter, HTTPException, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from sqlalchemy.orm import Session

from core.config import settings
from core.database import get_db
from routes.login import get_current_user


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix = "", tags=["Dashboard"],)


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    alert: Optional[str] = None,
    notification: Optional[str] = None
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)

        logout = "dashboard" in request.url.path
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return responses.RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request, name="website/dashboard.html",
        context={
            "app_environment": settings.APP_ENVIRONMENT,
            "alert": alert,
            "current_user": current_user,
            "logout": logout,
            "notification": notification,
        }
    )
