from sqlalchemy.orm import Session
from src.database.schema.account import Account

def get_all_accounts(db: Session):
    return db.query(Account).all()

def create_account(db: Session, account: Account):
    db.add(account)
    db.commit()
    db.refresh(account)
    return account