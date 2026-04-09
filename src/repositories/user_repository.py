from sqlmodel import Session, select
from src.database.schema.user import User

def get_all_users(db: Session):
    return db.exec(select(User)).all()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user