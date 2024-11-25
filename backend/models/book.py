from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional

from models.base_class import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Optional[str] = Column(Text, nullable=True)
    published_year = Optional[int] = Column(DateTime, nullable=True)
    done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    # # Creator relationship
    # creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # creator = relationship("User", back_populates="created_tasks", foreign_keys=[creator_id])
