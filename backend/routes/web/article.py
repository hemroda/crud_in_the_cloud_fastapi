from fastapi import APIRouter, Depends, Form, Request, Header, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from core.database import get_db
from service.article import ArticleService
from models.user import User
from routes.login import get_current_user
from core.config import settings


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix = "/articles", tags=["Website - Articles"])


@router.get("/", response_class=HTMLResponse)
async def tasks(
    request: Request,
    skip: int = 0,
    limit: int = 10,db: Session = Depends(get_db),
):
    articles = ArticleService.get_articles(db, skip, limit)

    return templates.TemplateResponse(
        request=request, name="website/articles/index.html",
        context={
            "articles": articles,
            "app_environment": settings.APP_ENVIRONMENT,
        }
    )
