from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


# =========================
# DATABASE MODEL
# =========================
class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id")
    role_id: int = Field(foreign_key="roles.id")

    email: str
    username: str
    password: str


# =========================
# REQUEST SCHEMAS
# =========================

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str


class AccountUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None


# =========================
# RESPONSE SCHEMA
# =========================

class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str

    class Config:
        from_attributes = True