from typing import Annotated, Optional

from fastapi import Depends, FastAPI, HTTPException, Query

from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(default=None, nullable=False, index=True)


