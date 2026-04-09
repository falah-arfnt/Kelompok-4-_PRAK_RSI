from sqlmodel import SQLModel, Field
from typing import Optional

class Registration(SQLModel, table=True):
    __tablename__ = "registrations"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")
    event_id: int = Field(foreign_key="events.id")