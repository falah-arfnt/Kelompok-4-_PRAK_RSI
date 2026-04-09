from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import role_controller
from src.dto.role_dto import RoleCreate

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return role_controller.get_roles(db)

@router.post("/")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_controller.create_role(db, role)