from sqlalchemy.orm import Session
from src.database.schema.event import EventCreate, EventUpdate

# sementara pakai dummy (kalau belum ada DB logic)
events = []

def get_events(db: Session):
    return events

<<<<<<< HEAD
def get_event_by_id(db: Session, event_id: int):
    return event_service.get_event_by_id(db, event_id)

def create_event(db: Session, event):
    return event_service.create_event(db, event)

def update_event(db: Session, event_id: int, event):
    return event_service.update_event(db, event_id, event)

def delete_event(db: Session, event_id: int):
    return event_service.delete_event(db, event_id)
=======
def create_event(db: Session, event: EventCreate):
    new_event = {
        "id": len(events) + 1,
        "name": event.name,
        "description": event.description
    }
    events.append(new_event)
    return new_event

def update_event(db: Session, id: int, event: EventUpdate):
    for e in events:
        if e["id"] == id:
            e["name"] = event.name
            e["description"] = event.description
            return e
    return {"error": "Event not found"}

def delete_event(db: Session, id: int):
    for e in events:
        if e["id"] == id:
            events.remove(e)
            return {"message": "Event deleted"}
    return {"error": "Event not found"}
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
