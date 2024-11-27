from sqlalchemy import Column, Integer, ForeignKey

from models.base_class import Base
from sqlalchemy.orm import relationship


class BookAuthor(Base):
    __tablename__ = "bookauthors"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    author = relationship("Author")
    book = relationship("Book")

    def __repr__(self):
        return f"<BookAuthor(id='{self.id}', author='{self.author}', book='{self.book}')>"
