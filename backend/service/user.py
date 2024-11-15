from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.user import UserCreate, UserShow, UserUpdate
import data.user as data


class UserService:
    @staticmethod
    def create_user(user: UserCreate, db: Session) -> UserShow:
        try:
            return data.db_create_user(user, db)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create user: {str(e)}"
            )


    @staticmethod
    def get_user_by_id(user_id: int, db: Session) -> UserShow:
        user = data.db_get_user_by_id(user_id, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return user


    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[UserShow]:
        return data.db_get_users(db, skip, limit)


    @staticmethod
    def update_user(
        user_id: int,
        user_data: UserUpdate,
        db: Session,
        partial: bool = False
    ) -> UserShow:
        existing_user = data.db_get_user_by_id(user_id, db)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        # Convert user_data to dict, excluding None values if partial update
        update_data = user_data.model_dump(
            exclude_unset=partial,  # True for PATCH, False for PUT
            exclude_none=partial
        )

        try:
            updated_user = data.db_update_user(user_id, update_data, db)
            return updated_user
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update user: {str(e)}"
            )


    @staticmethod
    def delete_user(user_id: int, db: Session) -> bool:
        if not data.db_delete_user(user_id, db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return True
