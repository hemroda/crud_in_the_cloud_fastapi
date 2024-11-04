from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from core.database import get_session
from models.task import Task
import data.task as service

router = APIRouter(prefix = "/tasks")

@router.get("/", response_model=list[Task])
def get_all(session: Session = Depends(get_session)) -> list[Task]:
    return service.get_all(session)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, session: Session = Depends(get_session)) -> Task:
    """Endpoint to get a task by its ID."""
    task = service.get_one(task_id, session)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=Task)
def create(task: Task, session: Session = Depends(get_session)) -> Task:
    return service.create(task, session)

@router.patch("/")
def modify(task: Task) -> Task:
    return service.modify(task)

@router.put("/")
def replace(task: Task) -> Task:
    return service.replace(task)

@router.delete("/{id}")
def delete(id: int):
    return service.delete(id)