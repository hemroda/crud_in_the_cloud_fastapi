from typing import Optional
from fastapi import Depends, Request, APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from sqlalchemy.orm import Session

from core.config import settings
from core.database import get_db
from routes.login import get_current_user

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="", tags=["Website"], )


@router.get("/", response_class=HTMLResponse)
async def homepage(
    request: Request,
    db: Session = Depends(get_db),
    alert: Optional[str] = None
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            current_user = None

    return templates.TemplateResponse(
        request=request, name="website/homepage.html",
        context={
            "app_environment": settings.APP_ENVIRONMENT,
            "alert": alert,
            "current_user": current_user,
        }
    )


# PORTFOLIO
from data.portfolio import technologies


@router.get("/portfolio", response_class=HTMLResponse)
async def portfolio(
    request: Request,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            current_user = None

    return templates.TemplateResponse(
        request=request, name="website/portfolio/index.html",
        context={"technologies": technologies, "current_user": current_user},
    )


@router.get("/portfolio/{techno_name}", response_class=HTMLResponse)
async def techno_info(techno_name: str):
    if techno_name in technologies:
        description_array = technologies[techno_name]['description']
        return "".join(
            "<li>" + description + "</li>" for description in description_array)
