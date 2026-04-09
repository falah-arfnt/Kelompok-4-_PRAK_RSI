from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
<<<<<<< HEAD
from src.controllers import event_controller
from src.dto.event_dto import EventCreate, EventUpdate, EventResponse
=======
from src.database.schema.event import Event
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

<<<<<<< HEAD
@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = event_controller.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_controller.create_event(db, event)

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = event_controller.get_event_by_id(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event_controller.update_event(db, event_id, event)

@router.patch("/{event_id}", response_model=EventResponse)
def patch_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = event_controller.get_event_by_id(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event_controller.update_event(db, event_id, event)

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = event_controller.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event_controller.delete_event(db, event_id)
    return {"message": "Event deleted successfully"}
=======
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
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
