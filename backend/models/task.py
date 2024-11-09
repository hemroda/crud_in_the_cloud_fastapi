from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.user import User


class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    user_id: int = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="tasks")
