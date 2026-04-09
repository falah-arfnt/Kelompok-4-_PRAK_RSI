from sqlalchemy.orm import Session
<<<<<<< HEAD
=======
from src.database.connection import get_db
from src.dto.role_dto import RoleCreate, RoleUpdate, RoleResponse
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
from src.services import role_service

def get_roles(db: Session):
    return role_service.get_roles(db)

def get_role_by_id(db: Session, role_id: int):
    return role_service.get_role_by_id(db, role_id)

def create_role(db: Session, role):
    return role_service.create_role(db, role)

def update_role(db: Session, role_id: int, role):
    return role_service.update_role(db, role_id, role)

def delete_role(db: Session, role_id: int):
    return role_service.delete_role(db, role_id)