from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: int = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
