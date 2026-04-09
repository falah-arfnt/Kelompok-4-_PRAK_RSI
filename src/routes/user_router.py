from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

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