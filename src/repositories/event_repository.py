from sqlalchemy.orm import Session
from src.database.schema.event import Event

def get_all_events(db: Session):
    return db.query(Event).all()

def get_event_by_id(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def create_event(db: Session, event: Event):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def update_event(db: Session, event_id: int, event_data: dict):
    event = get_event_by_id(db, event_id)
    if event:
        for key, value in event_data.items():
            if value is not None:
                setattr(event, key, value)
        db.commit()
        db.refresh(event)
    return event

def delete_event(db: Session, event_id: int):
    event = get_event_by_id(db, event_id)
    if event:
        db.delete(event)
        db.commit()
    return event