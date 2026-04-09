from sqlalchemy.orm import Session
from src.services import event_service

def get_events(db: Session):
    return event_service.get_events(db)

def create_event(db: Session, event):
    return event_service.create_event(db, event)