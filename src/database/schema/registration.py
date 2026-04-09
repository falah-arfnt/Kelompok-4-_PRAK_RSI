from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class Registration(SQLModel, table=True):
    __tablename__ = "registrations"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")
    event_id: int = Field(foreign_key="events.id")

class RegistrationCreate(BaseModel):
    user_id: int
    event_id: int

class RegistrationUpdate(BaseModel):
    user_id: int
    event_id: int

class RegistrationResponse(BaseModel):
    id: int
    user_id: int
    event_id: int

    class Config:
        from_attributes = True