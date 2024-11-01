from models.book import Book


_books = [
    Book(id=1,
        title="High-Performance Web Apps with FastAPI",
        description="""
            Build APIs and web apps based on Asynchronous Server Gateway Interface (ASGI). 
            This book provides a comprehensive explanation of using Pydantic models to construct the 
            request/response objects in a FASTAPI path operation. 
            You'll start by reviewing type hints in Python and the asynchronous processing concepts. 
            One of the highlights of FastAPI is its auto generation of API docs. 
            Pydantic library is the main pillar on top of which FastAPI is built.
        """
        ),
    Book(id=2,
        title="Building Python Microservices with FastAPI",
        description="""
            Discover the secrets of building Python microservices using the FastAPI framework. 
            Key Features:. Provides a reference that contains definitions, illustrations, comparative analysis, 
            and the implementation of real-world appsCovers concepts, core details, and advanced integration and 
            design-related topicsImparts context, app templates, suggestions, and insights that are helpful to 
            actual projects. 
            Book Description:. FastAPI is an Asynchronous Server Gateway Interface (ASGI)-based framework that 
            can help build modern, manageable, and fast microservices.        
        """
        ),
    Book(id=3,
        title="Building Python Web APIs with FastAPI",
        description="Book #1's description"),
    ]


def get_all() -> list[Book]:
    """ Return all books """
    return _books

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

def create(book: Book) -> Book:
    """Add a book"""
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
