from sqlalchemy.orm import Session
from src.database.schema.account import Account

def get_all_accounts(db: Session):
    return db.query(Account).all()

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account: Account):
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def update_account(db: Session, account_id: int, account_data: dict):
    account = get_account_by_id(db, account_id)
    if account:
        for key, value in account_data.items():
            if value is not None:
                setattr(account, key, value)
        db.commit()
        db.refresh(account)
    return account

def delete_account(db: Session, account_id: int):
    account = get_account_by_id(db, account_id)
    if account:
        db.delete(account)
        db.commit()
    return account