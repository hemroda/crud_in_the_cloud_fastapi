from fastapi import Depends
from sqlmodel import Session, select

from models.task import Task

from core.database import get_session


def get_all(session: Session = Depends(get_session)) -> list[Task]:
    """Retrieve all tasks from the database."""
    statement = select(Task)
    tasks = session.exec(statement).all()
    return [Task(name=task.name, description=task.description, id=task.id, user_id=task.user_id) for task in tasks]

def get_one(task_id: int, session: Session) -> Task | None:
    """Retrieve a task by its ID from the database."""
    statement = select(Task).where(Task.id == task_id)
    task = session.exec(statement).one_or_none()
    return task

def get_one_by_name(name: str) -> Task | None:
    for _task in _tasks:
        if _task.name == name:
            return _task
    return None

def create(task_data: Task, session: Session) -> Task:
    task = Task(name=task_data.name, description=task_data.description, user_id=task_data.user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def modify(task_id: int, task_data: Task, session: Session) -> Task | None:
    """Partially modify a task."""
    task = session.get(Task, task_id)
    if not task:
        return None

    if task_data.name is not None:
        task.name = task_data.name
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.user_id is not None:
        task.user_id = task_data.user_id

    session.add(task)
    session.commit()
    session.refresh(task)

    return task

def replace(task: Task) -> Task:
    """Completely replace a task"""
    return task

def delete(task_id: int, session: Session) -> bool:
    task = session.get(Task, task_id)
    session.delete(task)
    session.commit()
    return None
