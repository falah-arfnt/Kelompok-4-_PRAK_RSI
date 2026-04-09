from sqlalchemy.orm import Session
from src.repositories import event_repository
from src.database.schema.event import Event

def get_events(db: Session):
    return event_repository.get_all_events(db)

def get_event_by_id(db: Session, event_id: int):
    return event_repository.get_event_by_id(db, event_id)

def create_event(db: Session, event_data):
    event = Event(**event_data.dict())
    return event_repository.create_event(db, event)

def update_event(db: Session, event_id: int, event_data):
    return event_repository.update_event(db, event_id, event_data.dict(exclude_unset=True))

def delete_event(db: Session, event_id: int):
    return event_repository.delete_event(db, event_id)