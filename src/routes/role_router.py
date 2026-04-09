from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import role_controller
from src.dto.role_dto import RoleCreate, RoleUpdate, RoleResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return role_controller.get_roles(db)

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = role_controller.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_controller.create_role(db, role)

@router.put("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    db_role = role_controller.get_role_by_id(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(db, role_id, role)

@router.patch("/{role_id}", response_model=RoleResponse)
def patch_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    db_role = role_controller.get_role_by_id(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(db, role_id, role)

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = role_controller.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    role_controller.delete_role(db, role_id)
    return {"message": "Role deleted successfully"}