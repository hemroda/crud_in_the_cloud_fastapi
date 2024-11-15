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
