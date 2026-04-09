from sqlalchemy.orm import Session
from src.database.schema.account import Account

def get_all(db: Session):
    return db.query(Account).all()


def get_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()


# ✅ INI WAJIB ADA
def create(db: Session, data):
    account = Account(
        user_id=data.user_id,
        role_id=data.role_id,
        email=data.email,
        username=data.username,
        password=data.password
    )

    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def update(db: Session, account_id: int, data: dict):
    account = get_by_id(db, account_id)

    if not account:
        return None

    for key, value in data.items():
        if value is not None:
            setattr(account, key, value)

    db.commit()
    db.refresh(account)
    return account


def delete(db: Session, account_id: int):
    account = get_by_id(db, account_id)

    if not account:
        return None

    db.delete(account)
    db.commit()
    return account