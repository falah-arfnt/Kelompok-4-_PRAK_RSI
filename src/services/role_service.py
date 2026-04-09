from sqlalchemy.orm import Session
from src.repositories import role_repository
from src.database.schema.role import Role

def get_roles(db: Session):
    return role_repository.get_all_roles(db)

def get_role_by_id(db: Session, role_id: int):
    return role_repository.get_role_by_id(db, role_id)

def create_role(db: Session, role_data):
    role = Role(**role_data.dict())
    return role_repository.create_role(db, role)

def update_role(db: Session, role_id: int, role_data):
    return role_repository.update_role(db, role_id, role_data.dict(exclude_unset=True))

def delete_role(db: Session, role_id: int):
    return role_repository.delete_role(db, role_id)