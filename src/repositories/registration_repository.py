from sqlalchemy.orm import Session
from src.database.schema.registration import Registration

def get_all_registrations(db: Session):
    return db.query(Registration).all()

def create_registration(db: Session, registration: Registration):
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return registration