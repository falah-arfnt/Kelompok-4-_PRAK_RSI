from pydantic import BaseModel
from typing import Optional

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    username: str
    password: str

class AccountUpdate(BaseModel):
    user_id: Optional[int] = None
    role_id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None

class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    username: str

    class Config:
        from_attributes = True