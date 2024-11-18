from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.task import TaskCreate, TaskShow, TaskUpdate
import data.task as data

class TaskService:

    @staticmethod
    def create_task(task: TaskCreate, db: Session, creator_id) -> TaskShow:
        try:
            return data.db_create_task(task, db, creator_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create task: {str(e)}"
            )


    @staticmethod
    def get_task_by_id(task_id: int, db: Session) -> TaskShow:
        task = data.db_get_task_by_id(task_id, db)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"task with id {task_id} not found"
            )
        return task


    @staticmethod
    def get_tasks(db: Session, skip: int = 0, limit: int = 10) -> List[TaskShow]:
        return data.db_get_tasks(db, skip, limit)


    @staticmethod
    def update_task(
        task_id: int,
        task_data: TaskUpdate,
        db: Session,
        partial: bool = False
    ) -> TaskShow:
        existing_task = data.db_get_task_by_id(task_id, db)

        if not existing_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"task with id {task_id} not found"
            )

        # Convert task_data to dict, excluding None values if partial update
        update_data = task_data.model_dump(
            exclude_unset=partial,  # True for PATCH, False for PUT
            exclude_none=partial
        )

        try:
            updated_task = data.db_update_task(task_id, update_data, db)

            return updated_task

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update task: {str(e)}"
            )


    @staticmethod
    def delete_task(task_id: int, db: Session) -> bool:
        if not data.db_delete_task(task_id, db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"task with id {task_id} not found"
            )

        return True
