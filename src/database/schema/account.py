from sqlmodel import SQLModel, Field
from typing import Optional

class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")
    role_id: int = Field(foreign_key="roles.id")

    email: str
    username: str
    password: str