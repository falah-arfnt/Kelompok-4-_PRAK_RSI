from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
<<<<<<< HEAD
from src.database.connection import get_db
from src.controllers import user_controller
from src.dto.user_dto import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_controller.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.update_user(db, user_id, user)

@router.patch("/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.update_user(db, user_id, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_controller.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_controller.delete_user(db, user_id)
    return {"message": "User deleted successfully"}
=======

from src.database.connection import get_db
from src.database.schema.user import User

router = APIRouter(prefix="/users", tags=["Users"])

# ✅ GET (ambil semua user)
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ✅ POST (tambah user)
@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# ✅ PUT (update user)
@router.put("/{id}")
def update_user(id: int, user: User, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == id).first()

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_db.name = user.name
    db.commit()
    db.refresh(user_db)

    return user_db

# ✅ DELETE (hapus user)
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == id).first()

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user_db)
    db.commit()

    return {"message": "User deleted"}
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
