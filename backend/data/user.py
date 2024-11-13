from fastapi import Depends
from sqlmodel import Session, select

from models.user import User

from core.database import get_session


def get_all(session: Session = Depends(get_session)) -> list[User]:
    statement = select(User)
    users = session.exec(statement).all()
    return [User(email=user.email, id=user.id) for user in users]

def get_one(user_id: int, session: Session) -> User | None:
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).one_or_none()
    return user

def create(user_data: User, session: Session) -> User:
    user = User(email=user_data.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def modify(user_id: int, user_data: User, session: Session) -> User | None:
    user = session.get(User, user_id)

    if user is None:
        return None

    if user_data.email != user.email:
        user.email = user_data.email

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def delete(user_id: int, session: Session) -> bool:
    user = session.get(User, user_id)
    session.delete(user)
    session.commit()
    return None