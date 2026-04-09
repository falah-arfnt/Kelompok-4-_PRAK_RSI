from sqlalchemy.orm import Session
from src.database.schema.registration import Registration

def get_all_registrations(db: Session):
    return db.query(Registration).all()

def get_registration_by_id(db: Session, registration_id: int):
    return db.query(Registration).filter(Registration.id == registration_id).first()

def create_registration(db: Session, registration: Registration):
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return registration

def update_registration(db: Session, registration_id: int, registration_data: dict):
    registration = get_registration_by_id(db, registration_id)
    if registration:
        for key, value in registration_data.items():
            if value is not None:
                setattr(registration, key, value)
        db.commit()
        db.refresh(registration)
    return registration

def delete_registration(db: Session, registration_id: int):
    registration = get_registration_by_id(db, registration_id)
    if registration:
        db.delete(registration)
        db.commit()
    return registration