from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    quota: int

class EventCreate(BaseModel):
    name: str
    description: str

class EventUpdate(BaseModel):
    name: str
    description: str

class EventResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True