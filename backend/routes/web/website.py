from typing import Optional
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.config import settings


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix = "", tags=["Website"],)


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request, alert: Optional[str] = None):
    return templates.TemplateResponse(
        request=request, name="website/homepage.html",
        context={
            "app_environment": settings.APP_ENVIRONMENT,
            "alert": alert
        }
    )
