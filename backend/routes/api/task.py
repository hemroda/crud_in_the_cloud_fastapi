from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from models.user import User
from routes.login import get_current_user
from schemas.task import TaskCreate, TaskUpdate, TaskShow
from service.task import TaskService


router = APIRouter(
    prefix = "/api/tasks",
    tags=["API - Tasks"],
    responses={
        status.HTTP_201_CREATED: {"description": "Task has been created."},
        status.HTTP_404_NOT_FOUND: {"description": "Task not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    }
)


@router.get(
    "/",
    response_model=list[TaskShow],
    status_code=status.HTTP_200_OK,
    summary="Get all tasks",
    response_description="List of all tasks"
)
def get_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> List[TaskShow]:
    """Retrieve all tasks."""
    try:
        return TaskService.get_tasks(db, skip, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving tasks: {str(e)}"
        )


@router.get(
    "/{task_id}",
    response_model=TaskShow,
    status_code=status.HTTP_200_OK,
    summary="Get a specific task",
    response_description="The requested task"
)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)) -> TaskShow:
    """Retrieve a specific task by its ID."""
    try:
        task = TaskService.get_task_by_id(task_id, db)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        return task
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving task: {str(e)}"
        )


@router.post(
    "/",
    response_model=TaskShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    response_description="The created task"
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    response: Response = None
) -> TaskShow:
    """Create a task"""
    try:
        created_task = TaskService.create_task(task, db, creator_id=current_user.id)
        response.headers["Location"] = f"/tasks/{created_task.id}"

        return created_task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


@router.put(
    "/{task_id}",
    response_model=TaskShow,
    status_code=status.HTTP_200_OK,
    summary="Update an task (full update)"
)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
) -> TaskShow:
    """
    Update an task (full update).
    All fields must be provided.
    """
    return TaskService.update_task(
        task_id=task_id,
        task_data=task,
        db=db,
        partial=False
    )


@router.patch(
    "/{task_id}",
    response_model=TaskShow,
    status_code=status.HTTP_200_OK,
    summary="Update an task (partial update)"
)
def patch_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
) -> TaskShow:
    """
    Update an task (partial update).
    Only provided fields will be updated.
    """
    return TaskService.update_task(
        task_id=task_id,
        task_data=task,
        db=db,
        partial=True
    )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an task",
    response_description="Task successfully deleted"
)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Delete a task by its ID."""
    try:
        TaskService.delete_task(task_id, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )
