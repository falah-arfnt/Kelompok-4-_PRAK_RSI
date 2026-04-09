from sqlalchemy.orm import Session
from src.repositories import event_repository
from src.database.schema.event import Event

def get_events(db: Session):
    return event_repository.get_all_events(db)

def create_event(db: Session, event_data):
    event = Event(**event_data.dict())
    return event_repository.create_event(db, event)