from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import event_controller
from src.dto.event_dto import EventCreate

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return event_controller.get_events(db)

@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_controller.create_event(db, event)