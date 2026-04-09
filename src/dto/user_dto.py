from sqlmodel import SQLModel
from typing import Optional

class UserCreate(SQLModel):
    first_name: str
    last_name: Optional[str]
    whatsapp: Optional[str]