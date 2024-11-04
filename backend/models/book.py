from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str | None = None