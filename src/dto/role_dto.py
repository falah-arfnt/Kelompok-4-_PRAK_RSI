from pydantic import BaseModel
from typing import Optional

class RoleCreate(BaseModel):
    name: str

class RoleUpdate(BaseModel):
    name: Optional[str] = None

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
<<<<<<< HEAD
=======
        orm_mode = True

class RoleCreate(BaseModel):
    name: str

class RoleUpdate(BaseModel):
    name: str

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
        from_attributes = True