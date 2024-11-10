from fastapi import APIRouter, Depends
from sqlmodel import Session

from core.database import get_session
from models.book import Book
import data.book as service

router = APIRouter(prefix = "/books")

@router.get("/", response_model=list[Book])
def get_all(session: Session = Depends(get_session)) -> list[Book]:
    return service.get_all(session)

@router.get("/{id}")
def get_one(id) -> Book | None:
    return service.get_one(id)

@router.post("/")
def create(book: Book, session: Session = Depends(get_session)) -> Book:
    return service.create(book, session)

@router.patch("/")
def modify(book: Book) -> Book:
    return service.modify(book)

@router.put("/")
def replace(book: Book) -> Book:
    return service.replace(book)

@router.delete("/{id}")
def delete(id: int, session: Session = Depends(get_session)) -> dict:
    service.delete(id, session)

    return {"detail": "Book deleted succesfully."}
