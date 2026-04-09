from sqlalchemy.orm import Session
from src.services import account_service

def get_accounts(db: Session):
    return account_service.get_accounts(db)

def get_account_by_id(db: Session, account_id: int):
    return account_service.get_account_by_id(db, account_id)

def create_account(db: Session, account):
    return account_service.create_account(db, account)

def update_account(db: Session, account_id: int, account):
    return account_service.update_account(db, account_id, account)

def delete_account(db: Session, account_id: int):
    return account_service.delete_account(db, account_id)