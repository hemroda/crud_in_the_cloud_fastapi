from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import UserShow
import data.login as data

class LoginService:
    @staticmethod
    def get_user_by_email(user_email: str, db: Session) -> UserShow:
        user = data.db_get_user_by_email(user_email, db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"The user with email {user_email} not found"
            )

        return user
