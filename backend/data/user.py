from sqlalchemy.orm import Session

from schemas.user import UserCreate
from models.user import User
from core.hashing import Hasher


def db_get_users(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve all users"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users


def db_get_user_by_id(user_id: int, db: Session) -> User:
    """Retrieve a single user by its ID."""
    user = db.query(User).filter(User.id == user_id).first()
    return user


def db_create_user(user_data: UserCreate, db: Session) -> User:
    user = User(
        email=user_data.email,
        password=Hasher.get_password_hash(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def db_update_user(user_id: int, user_data: dict, db: Session) -> User:
    db_user = db_get_user_by_id(user_id, db)
    if db_user:
        for key, value in user_data.items():
            if value is not None:  # Only update fields that are provided
                setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def db_delete_user(user_id: int, db: Session) -> bool:
    """Delete a book"""
    user = db_get_user_by_id(user_id, db)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
