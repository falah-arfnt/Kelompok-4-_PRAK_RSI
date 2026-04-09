from sqlalchemy.orm import Session

def get_by_id(db: Session, model, id: int):
    return db.query(model).filter(model.id == id).first()

def update_data(db: Session, model, id: int, data: dict):
    obj = db.query(model).filter(model.id == id).first()
    if obj:
        for key, value in data.items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
    return obj

def delete_data(db: Session, model, id: int):
    obj = db.query(model).filter(model.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj