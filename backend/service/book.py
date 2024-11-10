from models.book import Book
import data.book as data


def get_all() -> list[Book]:
    return data.get_all()

def get_one(id: int) -> Book | None:
    return data.get_one(id)

def get_one_by_title(title: str) -> Book | None:
    return data.get_one_by_title(title)

def create(book: Book) -> Book:
    return data.create(book)

def replace(id, book: Book) -> Book:
    return data.replace(id, book)

def modify(id, book: Book) -> Book:
    return data.modify(id, book)

def delete(id: int) -> bool:
    return data.delete(id)