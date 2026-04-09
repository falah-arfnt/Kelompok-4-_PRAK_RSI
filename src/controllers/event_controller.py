from sqlalchemy.orm import Session
from src.database.schema.event import EventCreate, EventUpdate

# sementara pakai dummy (kalau belum ada DB logic)
events = []

def get_events(db: Session):
    return events

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