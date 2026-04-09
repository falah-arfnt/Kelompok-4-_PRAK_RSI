from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import role_controller
<<<<<<< HEAD
from src.dto.role_dto import RoleCreate, RoleUpdate, RoleResponse
=======
from src.database.schema.role import RoleCreate, RoleUpdate, RoleResponse
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return role_controller.get_roles(db)

<<<<<<< HEAD
@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = role_controller.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

=======
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_controller.create_role(db, role)

<<<<<<< HEAD
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
=======
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
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
