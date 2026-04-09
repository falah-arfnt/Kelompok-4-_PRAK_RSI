from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import role_controller
from src.database.schema.role import RoleCreate, RoleUpdate, RoleResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return role_controller.get_roles(db)

@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_controller.create_role(db, role)

@router.put("/{id}", response_model=RoleResponse)
def update_role(id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    return role_controller.update_role(db, id, role)

    if not role_db:
        raise HTTPException(status_code=404, detail="Role not found")

    role_db.name = role.name
    db.commit()
    db.refresh(role_db)

    return role_db

@router.delete("/{id}")
def delete_role(id: int, db: Session = Depends(get_db)):
    return role_controller.delete_role(db, id)

    if not role_db:
        raise HTTPException(status_code=404, detail="Role not found")

    db.delete(role_db)
    db.commit()

    return {"message": "Role deleted"}