from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


# =========================
# DATABASE MODEL (SQLModel)
# =========================
class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


# =========================
# SCHEMAS (Pydantic)
# =========================

class RoleCreate(BaseModel):
    name: str


class RoleUpdate(BaseModel):
    name: str


class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True