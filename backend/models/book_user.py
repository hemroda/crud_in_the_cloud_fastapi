from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_class import Base


class BookUser(Base):
    __tablename__ = "bookusers"

    id = Column(Integer, primary_key=True, index=True)
    finished = Column(Boolean, default=False)
    finished_at = Column(DateTime, nullable=True)
    started_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    user = relationship("User")
    book = relationship("Book")

    def __repr__(self):
        return f"<BookUser(id='{self.id}', user='{self.user}', book='{self.book}')>"
