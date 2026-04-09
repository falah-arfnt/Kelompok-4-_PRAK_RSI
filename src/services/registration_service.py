from sqlalchemy.orm import Session
from src.repositories import registration_repository
from src.database.schema.registration import Registration

def get_registrations(db: Session):
    return registration_repository.get_all_registrations(db)

def get_registration_by_id(db: Session, registration_id: int):
    return registration_repository.get_registration_by_id(db, registration_id)

def create_registration(db: Session, registration_data):
    registration = Registration(**registration_data.dict())
    return registration_repository.create_registration(db, registration)

def update_registration(db: Session, registration_id: int, registration_data):
    return registration_repository.update_registration(db, registration_id, registration_data.dict(exclude_unset=True))

def delete_registration(db: Session, registration_id: int):
    return registration_repository.delete_registration(db, registration_id)