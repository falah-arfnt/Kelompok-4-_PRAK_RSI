from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.schema.event import Event

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.post("/")
def create_event(event: Event, db: Session = Depends(get_db)):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.put("/{id}")
def update_event(id: int, event: Event, db: Session = Depends(get_db)):
    event_db = db.query(Event).filter(Event.id == id).first()

    if not event_db:
        raise HTTPException(status_code=404, detail="Event not found")

    event_db.name = event.name
    db.commit()
    db.refresh(event_db)

    return event_db

@router.delete("/{id}")
def delete_event(id: int, db: Session = Depends(get_db)):
    event_db = db.query(Event).filter(Event.id == id).first()

    if not event_db:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event_db)
    db.commit()

    return {"message": "Event deleted"}