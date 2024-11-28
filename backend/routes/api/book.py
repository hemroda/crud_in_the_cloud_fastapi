from fastapi import APIRouter, Depends, HTTPException, Path, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from models.book import Book
from schemas.book import BookCreate, BookUpdate, BookShow
from service.book import BookService


router = APIRouter(
    prefix="/api/books",
    tags=["API - Books"],
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    }
)


@router.get(
    "/",
    response_model=list[BookShow],
    status_code=status.HTTP_200_OK,
    summary="Get all books",
    response_description="List of all books"
)
def get_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> list[Book]:
    """Retrieve all books with optional filtering and pagination."""
    try:
        return BookService.get_books(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving books: {str(e)}"
        )


# @router.get(
#     "/{book_id}",
#     response_model=Book,
#     status_code=status.HTTP_200_OK,
#     summary="Get a specific book",
#     response_description="The requested book"
# )
# def get_one_by_id(
#     book_id: int = Path(..., title="Book ID", ge=1),
#     db: Session = Depends(get_db)
# ) -> Book:
#     """Retrieve a specific book by its ID."""
#     try:
#         book = service.get_one_by_id(book_id, session)
#         if book is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Book with ID {book_id} not found"
#             )
#         return book
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error retrieving book: {str(e)}"
#         )

@router.post(
    "/",
    response_model=BookShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    response_description="The created book"
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    response: Response = None
) -> Book:
    """Create a new book entry."""
    try:
        created_book = BookService.create_book(book, db)
        response.headers["Location"] = f"/books/{created_book.id}"

        return created_book
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating book: {str(e)}"
        )

# @router.patch(
#     "/",
#     response_model=Book,
#     status_code=status.HTTP_200_OK,
#     summary="Partially update a book",
#     response_description="The update book"
# )
# def modify(
#     book_id: int = Path(..., ge=1),
#     book: Book = None,
#     db: Session = Depends(get_db)
# ) -> Book:
#     """Partially update a book's information."""
#     try:
#         updated_book = service.modify(book)
#         if updated_book in None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Book with ID {book_id} not found"
#             )
#         return updated_book
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTENAL_SERVER_ERROR,
#             detail=f"Error updating book: {str(e)}"
#         )

# @router.put("/")
# def replace(book: Book) -> Book:
#     return service.replace(book)

# @router.delete(
#     "/{book_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     summary="Delete a book",
#     response_description="Book successfully deleted"
# )
# def delete(
#     book_id: int = Path(..., ge=1),
#     db: Session = Depends(get_db)
# ) -> None:
#     """Delete a book by its ID."""
#     try:
#         book = service.get_one_by_id(book_id, session)
#         if not book:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Book with ID {book_id} not found"
#             )
#         service.delete(book_id, session)
#     except HTTPException:
#         raise
#     except Exception as e:
#      raise HTTPException(
#           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#           detail=f"Error deleting book: {str(e)}"
#      )
