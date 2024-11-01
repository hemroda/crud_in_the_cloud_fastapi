from fastapi import APIRouter

# from models.book import Book

router = APIRouter(prefix = "/books")

# BOOKS
BOOKS = [
    {"id": 1, "title": "Book 1 title", "author": "Author 1", "description": "Book 1 description", "category": "math"},
    {"id": 2, "title": "Book 2 title", "author": "Author 2", "description": "Book 2 description", "category": "history"},
    {"id": 3, "title": "Book 3 title", "author": "Author 1", "description": "Book 3 description", "category": "math"},
]

@router.get("/")
async def get_books():

    return { "books": BOOKS }

@router.get("/{book_id:int}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.get("id") == book_id:
            
            return {"book": book}

    return {"message": "The book is not found."}

@router.get("/{book_title:str}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():

            return {"book": book}

    return {"message": "The book is not found."}