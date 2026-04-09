from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    whatsapp: str

    class Config:
        orm_mode = True