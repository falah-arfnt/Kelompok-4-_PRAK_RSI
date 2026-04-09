from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
<<<<<<< HEAD
from src.controllers import registration_controller
from src.dto.registration_dto import RegistrationCreate, RegistrationUpdate, RegistrationResponse

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/", response_model=list[RegistrationResponse])
def get_registrations(db: Session = Depends(get_db)):
    return registration_controller.get_registrations(db)

@router.get("/{registration_id}", response_model=RegistrationResponse)
def get_registration(registration_id: int, db: Session = Depends(get_db)):
    registration = registration_controller.get_registration_by_id(db, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration

@router.post("/", response_model=RegistrationResponse)
def create_registration(registration: RegistrationCreate, db: Session = Depends(get_db)):
    return registration_controller.create_registration(db, registration)

@router.put("/{registration_id}", response_model=RegistrationResponse)
def update_registration(registration_id: int, registration: RegistrationUpdate, db: Session = Depends(get_db)):
    db_registration = registration_controller.get_registration_by_id(db, registration_id)
    if not db_registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration_controller.update_registration(db, registration_id, registration)

@router.patch("/{registration_id}", response_model=RegistrationResponse)
def patch_registration(registration_id: int, registration: RegistrationUpdate, db: Session = Depends(get_db)):
    db_registration = registration_controller.get_registration_by_id(db, registration_id)
    if not db_registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration_controller.update_registration(db, registration_id, registration)

@router.delete("/{registration_id}")
def delete_registration(registration_id: int, db: Session = Depends(get_db)):
    registration = registration_controller.get_registration_by_id(db, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    registration_controller.delete_registration(db, registration_id)
    return {"message": "Registration deleted successfully"}
=======
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
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
