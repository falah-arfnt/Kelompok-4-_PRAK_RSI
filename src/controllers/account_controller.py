from sqlalchemy.orm import Session
from src.services import account_service

def get_accounts(db: Session):
    return account_service.get_accounts(db)

def create_account(db: Session, account):
    return account_service.create_account(db, account)