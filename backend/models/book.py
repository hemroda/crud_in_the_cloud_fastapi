from datetime import date, datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, ge=0)


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BookCreate(BookBase):
    pass


class BookUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1)
    author: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, ge=0)
    published_year: Optional[int] = Field(default_factory=lambda: date.today().year)
