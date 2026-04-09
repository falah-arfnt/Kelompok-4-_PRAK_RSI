from sqlalchemy.orm import Session
from src.repositories import registration_repository
from src.database.schema.registration import Registration

def get_registrations(db: Session):
    return registration_repository.get_all_registrations(db)

def create_registration(db: Session, registration_data):
    registration = Registration(**registration_data.dict())
    return registration_repository.create_registration(db, registration)