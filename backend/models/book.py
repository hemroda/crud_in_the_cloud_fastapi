# from datetime import date, datetime
# from typing import Optional
# from sqlalchemy import Column, Integer, String, Sequence

# from models.base_class import Base

# class BookBase(Base):
#     pass

# class Book():
#     pass

# class BookCreate(BookBase):
#     pass

# # class BookBase(Base):
# #     title: str = Column(String)
# #     author: str = Column(String)
# #     description: Optional[str] = None
# #     price: Optional[float] = Column(default=None)


# # class Book(BookBase, table=True):
# #     id: Optional[int] = Column(default=None, primary_key=True)
# #     created_at: datetime = Column(default_factory=datetime.utcnow)
# #     updated_at: datetime = Column(default_factory=datetime.utcnow)


# # class BookUpdate(sqlalchemy):
# #     title: Optional[str] = Column(default=None, min_length=1)
# #     author: Optional[str] = Column(default=None, min_length=1)
# #     description: Optional[str] = None
# #     price: Optional[float] = Column(default=None, ge=0)
# #     published_year: Optional[int] = Column(default_factory=lambda: date.today().year)
