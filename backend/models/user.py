from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from models.task import Task


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    email: str
    tasks: list["Task"] = Relationship(back_populates="user")
