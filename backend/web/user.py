from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from core.database import get_session
from models.user import User
import data.user as service

router = APIRouter(prefix = "/users")

@router.get("/", response_model=list[User])
def get_all(session: Session = Depends(get_session)) -> list[User]:

    return service.get_all(session)

@router.post("/", response_model=User)
def create(user: User, session: Session = Depends(get_session)) -> User:

    return service.create(user, session)

@router.patch("/{user_id}", response_model=User)
def modify(user_id: int, user: User, session: Session = Depends(get_session)) -> User:
    updated_user = service.modify(user_id, user, session)

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found.")

    return updated_user