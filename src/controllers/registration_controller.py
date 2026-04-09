from sqlalchemy.orm import Session
from src.services import registration_service

def get_registrations(db: Session):
    return registration_service.get_registrations(db)

def create_registration(db: Session, registration):
    return registration_service.create_registration(db, registration)