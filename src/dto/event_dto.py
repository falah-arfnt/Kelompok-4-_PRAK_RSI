from pydantic import BaseModel

class EventCreate(BaseModel):
    name: str
    description: str

class EventResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True