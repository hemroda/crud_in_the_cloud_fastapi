from typing import Annotated, Union
from fastapi import APIRouter, Depends, Form, Request, Header, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from core.database import get_db
from service.task import TaskService
from models.user import User
from schemas.task import TaskCreate
from routes.login import get_current_user
from core.config import settings

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix = "/tasks", tags=["Website - Tasks"],)


@router.get("/", response_class=HTMLResponse)
async def tasks(request: Request,):
   return templates.TemplateResponse(
            request=request, name="website/tasks/index.html",
            context={
                "app_environment": settings.APP_ENVIRONMENT
            }
        )


@router.get("/index/", response_class=HTMLResponse)
async def list_tasks(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    hx_request: Annotated[Union[str, None], Header()] = None
):
    tasks = TaskService.get_tasks(db, skip, limit)

    if hx_request:
        return templates.TemplateResponse(
            request=request, name="website/tasks/tasks.html", context={"tasks": tasks}
        )

    return JSONResponse(content=jsonable_encoder(tasks))


@router.post("/", response_class=HTMLResponse)
async def create_task(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    task_name: str = Form(...),
    description: str = Form(default=""),
):
    try:
        # Create a TaskCreate instance with the form data
        task_data = TaskCreate(name=task_name, description=description)
        TaskService.create_task(task_data, db, creator_id=current_user.id)
        tasks = TaskService.get_tasks(db, skip, limit)

        return templates.TemplateResponse(
            request=request,
            name="website/partials/task-list.html"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )
