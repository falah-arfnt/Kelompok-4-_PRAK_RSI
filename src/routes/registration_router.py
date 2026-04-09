from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.schema.registration import Registration

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/")
def get_registrations(db: Session = Depends(get_db)):
    return db.query(Registration).all()

@router.post("/")
def create_registration(registration: Registration, db: Session = Depends(get_db)):
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return registration

@router.put("/{id}")
def update_registration(id: int, registration: Registration, db: Session = Depends(get_db)):
    reg_db = db.query(Registration).filter(Registration.id == id).first()

    if not reg_db:
        raise HTTPException(status_code=404, detail="Registration not found")

    reg_db.user_id = registration.user_id
    reg_db.event_id = registration.event_id

    db.commit()
    db.refresh(reg_db)

    return reg_db

@router.delete("/{id}")
def delete_registration(id: int, db: Session = Depends(get_db)):
    reg_db = db.query(Registration).filter(Registration.id == id).first()

    if not reg_db:
        raise HTTPException(status_code=404, detail="Registration not found")

    db.delete(reg_db)
    db.commit()

    return {"message": "Registration deleted"}