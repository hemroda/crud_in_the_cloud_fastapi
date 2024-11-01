from fastapi import APIRouter

from models.book import Book
import data.book as service

router = APIRouter(prefix = "/books")

@router.get("/")
def get_all() -> list[Book]:
    return service.get_all()

@router.get("/{id}")
def get_one(id) -> Book | None:
    return service.get_one(id)

@router.post("/")
def create(book: Book) -> Book:
    return service.create(book)

@router.patch("/")
def modify(book: Book) -> Book:
    return service.modify(book)

@router.put("/")
def replace(book: Book) -> Book:
    return service.replace(book)

@router.delete("/{id}")
def delete(id: int):
    return service.delete(id)
