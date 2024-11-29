from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.book import BookCreate, BookShow, BookUpdate
import data.book as data


class BookService:

    @staticmethod
    def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[BookShow]:
        return data.db_get_books(db, skip, limit)

    @staticmethod
    def create_book(book: BookCreate, db: Session, ) -> BookShow:
        try:
            return data.db_create_book(book, db)
        except ValueError as ve:
            # Handle specific case of duplicate book
            raise HTTPException(
                # Use 409 Conflict for duplicate resources
                status_code=status.HTTP_409_CONFLICT,
                detail=str(ve)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create book: {str(e)}"
            )

    @staticmethod
    def get_book_by_id(book_id: int, db: Session) -> BookShow:
        book = data.db_get_book_by_id(book_id, db)

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"book with id {book_id} not found"
            )

        return book

    @staticmethod
    def update_book(
        book_id,
        book_data: BookUpdate,
        db: Session,
        partial: bool = False
    ) -> BookShow:
        existing_book = data.db_get_book_by_id(book_id, db)

        if not existing_book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found"
            )

        # Convert book_data to dict, excluding None values if partial update
        update_data = book_data.model_dump(
            exclude_unset=partial,  # True for PATCH, False for PUT
            exclude_none=partial
        )

        try:
            updated_book = data.db_update_book(book_id, update_data, db)

            return updated_book
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update the book: {str(e)}"
            )

    @staticmethod
    def delete_book(book_id: int, db: Session) -> bool:
        if not data.db_delete_book(book_id, db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id {book_id} not found"
            )

        return True
