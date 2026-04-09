from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database.connection import get_session
from src.services import user_service
from src.dto.user_dto import UserCreate

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_session)):
    return user_service.get_users(db)

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    return user_service.create_user(db, user)