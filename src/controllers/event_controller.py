from sqlalchemy.orm import Session
from src.services import event_service

def get_events(db: Session):
    return event_service.get_events(db)

def get_event_by_id(db: Session, event_id: int):
    return event_service.get_event_by_id(db, event_id)

def create_event(db: Session, event):
    return event_service.create_event(db, event)

def update_event(db: Session, event_id: int, event):
    return event_service.update_event(db, event_id, event)

def delete_event(db: Session, event_id: int):
    return event_service.delete_event(db, event_id)
