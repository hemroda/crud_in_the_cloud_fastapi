from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime


class AuthorCreate(BaseModel):
    first_name: constr(min_length=3, max_length=200)
    last_name: constr(min_length=3, max_length=200)


class AuthorShow(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class AuthorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    updated_at: Optional[datetime] = None
