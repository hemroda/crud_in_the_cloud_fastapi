from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="tasks")

# Define relationship after class declarations to avoid circular import issues
from models.user import User
Task.user = Relationship(back_populates="tasks")