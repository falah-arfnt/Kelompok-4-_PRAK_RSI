from sqlalchemy.orm import Session
from src.repositories import user_repository
from src.database.schema.user import User

def get_users(db: Session):
    return user_repository.get_all_users(db)

def create_user(db: Session, user_data):
    user = User(**user_data.dict())
    return user_repository.create_user(db, user)