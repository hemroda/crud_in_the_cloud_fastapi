from sqlalchemy.orm import Session

from schemas.user import UserShow
from models.user import User

def db_get_user_by_email(user_email: str, db: Session) -> User:
    """Retrieve a single user by its email."""

    user = db.query(User).filter(User.email == user_email).first()

    return user
