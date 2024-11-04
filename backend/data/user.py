from fastapi import Depends
from sqlmodel import Session, select

from models.user import User

from core.database import get_session


def get_all(session: Session = Depends(get_session)) -> list[User]:
    """Retrieve all users from the database."""
    statement = select(User)
    users = session.exec(statement).all()  # Use the session instance to execute
    return [User(email=user.email) for user in users]

def create(user_data: User, session: Session) -> User:
    user = User(email=user_data.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user