from fastapi import Depends
from sqlmodel import Session, select

from models.task import Task

from core.database import get_session


def get_all(session: Session = Depends(get_session)) -> list[Task]:
    """Retrieve all tasks from the database."""
    statement = select(Task)
    tasks = session.exec(statement).all()  # Use the session instance to execute
    return [Task(name=task.name, description=task.description, id=task.id) for task in tasks]

def get_one(id: int, session: Session) -> Task | None:
    """Retrieve a task by its ID from the database."""
    statement = select(Task).where(Task.id == id)
    task = session.exec(statement).one_or_none()
    return task

def get_one_by_name(name: str) -> Task | None:
    for _task in _tasks:
        if _task.name == name:
            return _task
    return None

def create(task_data: Task, session: Session) -> Task:
    task = Task(name=task_data.name, description=task_data.description, id=task_data.id, user_id=task_data.user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def modify(task: Task) -> Task:
    """Partially modify a task"""
    return task

def replace(task: Task) -> Task:
    """Completely replace a task"""
    return task

def delete(name: str) -> bool:
    """Delete a task; return None if it existed"""
    return None
