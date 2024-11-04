from fastapi import Depends
from sqlmodel import Session, select

from models.book import Book

from core.database import get_session


def get_all(session: Session = Depends(get_session)) -> list[Book]:
    statement = select(Book)
    books = session.exec(statement).all()
    return [Book(title=book.title, description=book.description,) for book in books]

def get_one(id: int) -> Book | None:
    for _book in _books:
        if _book.id == int(id):
            return _book
    return None

def get_one_by_title(title: str) -> Book | None:
    for _book in _books:
        if _book.title == title:
            return _book
    return None

def create(book_data: Book, session: Session) -> Book:
    """Add a book"""
    book = Book(**book_data.dict())
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def modify(book: Book) -> Book:
    """Partially modify a book"""
    return book

def replace(book: Book) -> Book:
    """Completely replace a book"""
    return book

def delete(name: str) -> bool:
    """Delete a book return None if it existed"""
    return None
