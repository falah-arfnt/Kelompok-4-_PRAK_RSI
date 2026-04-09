from sqlalchemy.orm import Session
from src.repositories import user_repository
from src.database.schema.user import User

def get_users(db: Session):
    return user_repository.get_all_users(db)

def get_user_by_id(db: Session, user_id: int):
    return user_repository.get_user_by_id(db, user_id)

def create_user(db: Session, user_data):
    user = User(**user_data.dict())
    return user_repository.create_user(db, user)

def update_user(db: Session, user_id: int, user_data):
    return user_repository.update_user(db, user_id, user_data.dict(exclude_unset=True))

def delete_user(db: Session, user_id: int):
    return user_repository.delete_user(db, user_id)