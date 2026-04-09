from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True