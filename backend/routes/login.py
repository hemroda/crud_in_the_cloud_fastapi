from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from core.config import settings
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


oath2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(
    token: str = Depends(oath2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials. Please login again."
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = LoginService.get_user_by_email(user_email=email, db=db)

    if user is None:
        raise credentials_exception

    return user


# Login Routes
import json
from fastapi.templating import Jinja2Templates
from fastapi import Request, responses, Form
from pydantic import ValidationError

from schemas.user import UserCreate
from service.user import UserService


templates = Jinja2Templates(directory="templates")


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse(request=request, name="auth/register.html")


@router.post("/register")
def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user_data = UserCreate(email=email, password=password)
        UserService.create_user(user=user_data, db=db)

        return responses.RedirectResponse(
            "/?alert=Successfully%20Registered",
            status_code=status.HTTP_302_FOUND
        )
    except ValidationError as e:
        # Parse Pydantic validation errors
        errors = [
            f"{error['loc'][0]}: {error['msg']}"
            for error in e.errors()
        ]
        return templates.TemplateResponse(
            "auth/register.html",
            {
                "request": request,
                "errors": errors,
                "email": email  # Preserve entered email
            }
        )
    except Exception as e:
        # Handle other unexpected errors
        return templates.TemplateResponse(
            "auth/register.html",
            {
                "request": request,
                "errors": [str(e)],
                "email": email
            }
        )


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse(request=request, name="auth/login.html")


@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    errors = []
    user = authenticate_user(email, password, db)

    if not user:
        errors.append("Incorrect email or password")

        return templates.TemplateResponse(
            request=request, name="auth/login.html",
            context={ "errors": errors }
        )

    access_token = create_access_token(data={"sub": user.email})
    response = responses.RedirectResponse(
        "/?alert=Successfully Logged in",
        status_code=status.HTTP_302_FOUND
    )
    response.set_cookie(key="access_token", value=f"Bearer {access_token}")

    return response
