# from fastapi import APIRouter, Depends, HTTPException, Path, Response, status

# from models.book import Book
# import data.book as service

# router = APIRouter(
#     prefix = "/books",
#     tags=["Books"],
#     responses={
#         status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
#     }
# )

# @router.get(
#     "/",
#     response_model=list[Book],
#     status_code=status.HTTP_200_OK,
#     summary="Get all books",
#     response_description="List of all books"
# )
# def get_all(
#         session: Session = Depends(get_session),
#         skip: int = 0,
#         limit: int = 100
#     ) -> list[Book]:
#     """
#     Retrieve all books with optional filtering and pagination.

#     Parameters:
#         skip: Number of records to skip
#         limit: Maximum number of records to return
#     """
#     try:
#         return service.get_all(session, skip=skip, limit=limit)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error retrieving books: {str(e)}"
#         )

# @router.get(
#     "/{book_id}",
#     response_model=Book,
#     status_code=status.HTTP_200_OK,
#     summary="Get a specific book",
#     response_description="The requested book"
# )
# def get_one_by_id(
#     book_id: int = Path(..., title="Book ID", ge=1),
#     session: Session = Depends(get_session)
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

# @router.post(
#     "/",
#     response_model=Book,
#     status_code=status.HTTP_201_CREATED,
#     summary="Create a new book",
#     response_description="The created book"
# )
# def create(
#     book: Book,
#     session: Session = Depends(get_session),
#     response: Response = None
# ) -> Book:
#     """Create a new book entry."""
#     try:
#         book = service.create(book, session)
#         response.headers["Location"] = f"/books/{book.id}"
#         return book
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error creating book: {str(e)}"
#         )

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
#     session: Session = Depends(get_session)
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
#     response_description="Book succesfully deleted"
# )
# def delete(
#     book_id: int = Path(..., ge=1),
#     session: Session = Depends(get_session)
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
