from sqlalchemy.orm import Session
from src.database.schema.role import Role

def get_all_roles(db: Session):
    return db.query(Role).all()

def create_role(db: Session, role: Role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role