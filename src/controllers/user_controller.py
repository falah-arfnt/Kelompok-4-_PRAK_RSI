from sqlalchemy.orm import Session
from src.services import user_service

def get_users(db: Session):
    return user_service.get_users(db)

def create_user(db: Session, user):
    return user_service.create_user(db, user)