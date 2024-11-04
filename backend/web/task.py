from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.database import get_session
from data.task import get_all

from models.task import Task

import data.task as service

router = APIRouter(prefix = "/tasks")

@router.get("/", response_model=list[Task])
def get_all_tasks(session: Session = Depends(get_session)) -> list[Task]:
    return get_all(session)

@router.get("/{id}")
def get_one(id) -> Task | None:
    return service.get_one(id)

@router.post("/")
def create(task: Task) -> Task:
    return service.create(task)

@router.patch("/")
def modify(task: Task) -> Task:
    return service.modify(task)

@router.put("/")
def replace(task: Task) -> Task:
    return service.replace(task)

@router.delete("/{id}")
def delete(id: int):
    return service.delete(id)