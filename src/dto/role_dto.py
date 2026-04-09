from pydantic import BaseModel

class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    username: str
    password: str

class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    username: str

    class Config:
        orm_mode = True

class RoleCreate(BaseModel):
    name: str

class RoleUpdate(BaseModel):
    name: str

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True