from pydantic import BaseModel
from typing import Optional


# CREATE
class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str


# UPDATE
class AccountUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None


# RESPONSE
class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str

    class Config:
        from_attributes = True