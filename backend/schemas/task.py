from typing import Optional, Text
from pydantic import BaseModel, constr
from datetime import datetime


class TaskCreate(BaseModel):
    name: constr(min_length=3, max_length=200)
    description: Optional[Text]


class TaskShow(BaseModel):
    id: int
    name: str
    description: Optional[Text] = None
    created_at: datetime
    done_at: Optional[datetime]
    done: bool
    updated_at: Optional[datetime]
    creator_id: int
    owner_id: Optional[int]

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description:  Optional[Text] = None
    updated_at: datetime  = None
    done_at: datetime  = None
    done: Optional[bool] = None
    owner_id: Optional[int] = None
