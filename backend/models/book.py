from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Text
from typing import Optional

from models.base_class import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False, unique=True)
    description: Optional[str] = Column(Text, nullable=True)
    added_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    published_year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title})>"
