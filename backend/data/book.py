from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.book import Book
from schemas.book import BookCreate, BookShow, BookUpdate


def db_get_books(db: Session, skip: int = 0, limit: int = 10) -> list[BookShow]:
    """Retrieve all books"""
    books = db.query(Book).offset(skip).limit(limit).all()

    return books


def db_get_book_by_id(book_id: int, db: Session) -> Book:
    """Retrieve a single book by its ID."""
    book = db.query(Book).filter(Book.id == book_id).first()

    return book


def db_create_book(book_data: BookCreate, db: Session) -> Book:
    """Create a new book"""
    db_book = Book(**book_data.dict())
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except IntegrityError as e:
        db.rollback()
        # More specific error handling for unique constraint
        if 'UniqueViolation' in str(e):
            raise ValueError(f"A book with the title '{book_data.title}' already exists")
        raise
    except Exception as e:
        db.rollback()
        raise Exception(f"Failed to create book: {str(e)}")


def db_update_book(book_id: int, book_data: BookUpdate, db: Session) -> Book:
    """Update a book"""
    db_book = db_get_book_by_id(book_id, db)

    if db_book:

        for key, value in book_data.items():
            if value is not None:
                setattr(db_book, key, value)

        db.commit()
        db.refresh(db_book)

    return db_book


def db_delete_book(book_id: int, db: Session) -> bool:
    """Delete a book"""
    book = db_get_book_by_id(book_id, db)

    if book:
        db.delete(book)
        db.commit()
        return True

    return False
