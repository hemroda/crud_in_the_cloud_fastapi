from fastapi import FastAPI
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    description: str | None = None