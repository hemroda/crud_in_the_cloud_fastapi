# from datetime import datetime
# from fastapi import Depends, HTTPException
# from sqlalchemy import select

# from models.book import Book, BookCreate, BookUpdate




# def get_all(session: Session = Depends(get_session), skip: int = 0, limit: int = 100) -> list[Book]:
#     statement = select(Book).offset(skip).limit(limit)
#     books = session.exec(statement).all()
#     return [Book(title=book.title, description=book.description,id=book.id) for book in books]

# def get_one_by_id(book_id: int, session: Session) -> Book | None:
#     statement = select(Book).where(Book.id == book_id)
#     book = session.exec(statement).one_or_none()
#     return book

# def create(book_data: BookCreate, session: Session) -> Book:
#     """Create a new book"""
#     db_book = Book.from_orm(book_data)
#     db_book.created_at = datetime.utcnow()
#     db_book.updated_at = datetime.utcnow()

#     session.add(db_book)
#     session.commit()
#     session.refresh(db_book)

#     return db_book

# def modify(book_id: int, book_update: BookUpdate, session: Session) -> Book:
#     """Partially modify a book"""
#     db_book = get_one_by_id(book_id, session)
#     if not db_book:
#         raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

#     update_data = book_update.dict(exclude_unset=True)
#     for field, value in update_data.items():
#         setattr(db_book, field, value)

#     db_book.updated_at = datetime.utcnow()

#     session.add(db_book)
#     session.commit()
#     session.refresh(db_book)

#     return db_book

# def replace(book_id: int, book_data: BookCreate, session: Session) -> Book:
#     """Completely replace a book"""
#     # Get existing book
#     db_book = get_one_by_id(book_id, session)
#     if not db_book:
#         raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

#     # Update all fields
#     book_dict = book_data.dict()
#     for field, value in book_dict.items():
#         setattr(db_book, field, value)

#     # Update timestamp
#     db_book.updated_at = datetime.now(datetime.timezone.utc)

#     session.add(db_book)
#     session.commit()
#     session.refresh(db_book)

#     return db_book

# def delete(book_id: int, session: Session) -> bool:
#     """Delete a book"""

#     db_book = get_one_by_id(book_id, session)
#     if not db_book:
#         return False

#     session.delete(db_book)
#     session.commit()

#     return True
