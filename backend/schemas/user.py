from typing import Optional, Text
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserShow(BaseModel):
    id: int
    email: EmailStr
    admin: bool

    class Config():
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    admin: Optional[bool] = None
