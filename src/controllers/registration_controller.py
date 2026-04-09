from sqlalchemy.orm import Session
from src.services import registration_service

def get_registrations(db: Session):
    return registration_service.get_registrations(db)

def get_registration_by_id(db: Session, registration_id: int):
    return registration_service.get_registration_by_id(db, registration_id)

def create_registration(db: Session, registration):
    return registration_service.create_registration(db, registration)

def update_registration(db: Session, registration_id: int, registration):
    return registration_service.update_registration(db, registration_id, registration)

def delete_registration(db: Session, registration_id: int):
    return registration_service.delete_registration(db, registration_id)
