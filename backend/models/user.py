from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.task import Task


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    tasks: list["Task"] = Relationship(back_populates="user")


# Define relationship after class declarations to avoid circular import issues
from models.task import Task
User.tasks = Relationship(back_populates="user")