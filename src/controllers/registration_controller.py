from sqlalchemy.orm import Session
from src.database.schema.registration import RegistrationCreate, RegistrationUpdate

registrations = []

def get_registrations(db: Session):
    return registrations

def create_registration(db: Session, registration: RegistrationCreate):
    new_reg = {
        "id": len(registrations) + 1,
        "user_id": registration.user_id,
        "event_id": registration.event_id
    }
    registrations.append(new_reg)
    return new_reg

def update_registration(db: Session, id: int, registration: RegistrationUpdate):
    for r in registrations:
        if r["id"] == id:
            r["user_id"] = registration.user_id
            r["event_id"] = registration.event_id
            return r
    return {"error": "Registration not found"}

def delete_registration(db: Session, id: int):
    for r in registrations:
        if r["id"] == id:
            registrations.remove(r)
            return {"message": "Registration deleted"}
    return {"error": "Registration not found"}