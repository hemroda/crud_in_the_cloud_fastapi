from typing import Optional

from pydantic import BaseModel

from models.author import Author
from models.book import Book


class BookAuthorCreate(BaseModel):
    author: Author
    book: Book


class BookAuthorShow(BaseModel):
    author: Author
    book: Book

    class Config:
        from_attribute = True


class BookAuthorUpdate(BaseModel):
    author: Optional[Author] = None
    book: Optional[Book] = None
