from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String

from models.base_class import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=60), nullable=False)
    last_name = Column(String(length=60), nullable=False)
    added_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return "<Author(author_id='{0}', first_name='{1}', last_name='{2}'>".format(
            self.id, self.first_name, self.last_name)
