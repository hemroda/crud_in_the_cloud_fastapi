from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt

from core.database import get_db
from core.hashing import Hasher
from core.security import create_access_token
from service.login import LoginService

router = APIRouter(tags=["Authentication"],)

def authenticate_user(email: str, password: str, db: Session):
    user = LoginService.get_user_by_email(user_email=email, db=db)

    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False

    return user


@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
