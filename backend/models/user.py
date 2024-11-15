from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from models.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    articles = relationship("Article", back_populates="author")
    # tasks: list["Task"] = Relationship(back_populates="user")
