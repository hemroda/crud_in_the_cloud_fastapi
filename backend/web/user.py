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
