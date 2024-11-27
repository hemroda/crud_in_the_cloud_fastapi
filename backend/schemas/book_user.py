from typing import Optional

from pydantic import BaseModel

from models.user import User
from models.book import Book


class BookUserCreate(BaseModel):
    user: User
    book: Book


class BookUserShow(BaseModel):
    user: User
    book: Book

    class Config:
        from_attribute = True


class BookUserUpdate(BaseModel):
    user: Optional[User] = None
    book: Optional[Book] = None
