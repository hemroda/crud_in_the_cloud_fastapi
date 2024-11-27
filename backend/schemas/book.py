from pydantic import BaseModel, constr
from typing import Optional, Text
from datetime import datetime


class BookCreate(BaseModel):
    title: constr(min_length=3, max_length=220)
    description: Optional[Text]


class BookShow(BaseModel):
    id: int
    title: str
    description: Optional[Text] = None

    class Config:
        from_attribute = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[Text] = None
    updated_at:  Optional[datetime] = None
    published_year: Optional[datetime] = None
