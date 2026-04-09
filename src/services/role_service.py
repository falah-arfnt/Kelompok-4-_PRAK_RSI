from sqlalchemy.orm import Session
from src.repositories import role_repository
from src.database.schema.role import Role

def get_roles(db: Session):
    return role_repository.get_all_roles(db)

def create_role(db: Session, role_data):
    role = Role(**role_data.dict())
    return role_repository.create_role(db, role)