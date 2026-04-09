from sqlalchemy.orm import Session
from src.services import user_service

def get_users(db: Session):
    return user_service.get_users(db)

def get_user_by_id(db: Session, user_id: int):
    return user_service.get_user_by_id(db, user_id)

def create_user(db: Session, user):
    return user_service.create_user(db, user)

def update_user(db: Session, user_id: int, user):
    return user_service.update_user(db, user_id, user)

def delete_user(db: Session, user_id: int):
    return user_service.delete_user(db, user_id)