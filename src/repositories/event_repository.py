from sqlalchemy.orm import Session
from src.database.schema.event import Event

def get_all_events(db: Session):
    return db.query(Event).all()

def create_event(db: Session, event: Event):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event