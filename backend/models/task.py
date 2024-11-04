from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    user: "User" = Relationship(back_populates="tasks")
    user_id: int = Field(default=None, foreign_key="user.id")

# Define relationship after class declarations to avoid circular import issues
from models.user import User
Task.user = Relationship(back_populates="tasks")