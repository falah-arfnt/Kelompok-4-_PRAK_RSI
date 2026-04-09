from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from src.database import get_session
from src.models import Event
from src.schemas.event import EventCreate, EventUpdate, EventResponse

router = APIRouter(prefix="/events", tags=["Events"])

# 1. GET ALL (Mengambil semua daftar event) - 200 OK
@router.get("/", response_model=List[EventResponse])
def read_events(session: Session = Depends(get_session)):
    events = session.exec(select(Event)).all()
    return events

# 2. POST (Membuat event baru) - 201 Created
@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(event_data: EventCreate, session: Session = Depends(get_session)):
    db_event = Event.model_validate(event_data)
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    return db_event

# 3. GET BY ID (Melihat detail satu event) - 200 OK
@router.get("/{id}", response_model=EventResponse)
def read_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    return event

# 4. PUT (Mengupdate data event) - 200 OK
@router.put("/{id}", response_model=EventResponse)
def update_event(id: int, event_data: EventUpdate, session: Session = Depends(get_session)):
    db_event = session.get(Event, id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    
    data = event_data.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_event, key, value)
        
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    return db_event

# 5. DELETE (Menghapus event) - 204 No Content
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    session.delete(event)
    session.commit()
    return None