from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
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