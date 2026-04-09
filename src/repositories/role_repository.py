from sqlalchemy.orm import Session
from src.database.schema.role import Role

def get_all_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def create_role(db: Session, role: Role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def update_role(db: Session, role_id: int, role_data: dict):
    role = get_role_by_id(db, role_id)
    if role:
        for key, value in role_data.items():
            if value is not None:
                setattr(role, key, value)
        db.commit()
        db.refresh(role)
    return role

def delete_role(db: Session, role_id: int):
    role = get_role_by_id(db, role_id)
    if role:
        db.delete(role)
        db.commit()
    return role