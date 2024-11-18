from sqlalchemy.orm import Session
from datetime import datetime

from schemas.task import TaskCreate
from models.task import Task


def db_get_tasks(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve all tasks"""
    tasks = db.query(Task).offset(skip).limit(limit).all()

    return tasks


def db_get_task_by_id(task_id: int, db: Session) -> Task:
    """Retrieve a single task by its ID."""
    task = db.query(Task).filter(Task.id == task_id).first()

    return task


def db_create_task(task_data: TaskCreate,db: Session, creator_id) -> Task:
    """Create a new task"""
    db_task = Task(
        name=task_data.name,
        description=task_data.description,
        creator_id=creator_id,
        done=False
    )
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    except Exception as e:
        db.rollback()
        raise Exception(f"Failed to create task: {str(e)}")


def db_update_task(task_id: int, task_data: dict, db: Session) -> Task:
    """Update a task"""
    db_task = db_get_task_by_id(task_id, db)

    if db_task:
        for key, value in task_data.items():
            if value is not None:  # Only update fields that are provided
                setattr(db_task, key, value)

        # Set updated_at whenever any update occurs
        db_task.updated_at = datetime.now()

        # If task is being marked as done, set done_at
        if db_task.done is True:
            db_task.done_at = datetime.now()

        db.commit()
        db.refresh(db_task)

    return db_task


def db_delete_task(task_id: int, db: Session) -> bool:
    """Delete a task"""
    task = db_get_task_by_id(task_id, db)

    if task:
        db.delete(task)
        db.commit()

        return True

    return False
