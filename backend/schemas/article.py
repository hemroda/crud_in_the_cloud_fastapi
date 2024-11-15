# backend/schemas/article.py

from typing import Optional, Text
from pydantic import BaseModel, constr, validator, root_validator
from datetime import datetime


class ArticleCreate(BaseModel):
    title: constr(min_length=3, max_length=100)
    slug: constr(min_length=3, max_length=100)
    content: Text
    author_id: int

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ArticleShow(BaseModel):
    id: int
    title: str
    content: Text
    created_at: datetime
    published: bool

    class Config():
        from_attributes = True


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
