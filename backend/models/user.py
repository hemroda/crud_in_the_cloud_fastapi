from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from models.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

    articles = relationship("Article", back_populates="author")
    created_tasks = relationship("Task", back_populates="creator",foreign_keys="Task.creator_id")
    owned_tasks = relationship("Task", back_populates="owner",foreign_keys="Task.owner_id")
