from sqlalchemy.orm import Session
from src.repositories import account_repository
from src.database.schema.account import Account

def get_accounts(db: Session):
    return account_repository.get_all_accounts(db)

def get_account_by_id(db: Session, account_id: int):
    return account_repository.get_account_by_id(db, account_id)

def create_account(db: Session, account_data):
    account = Account(**account_data.dict())
    return account_repository.create_account(db, account)

def update_account(db: Session, account_id: int, account_data):
    return account_repository.update_account(db, account_id, account_data.dict(exclude_unset=True))

def delete_account(db: Session, account_id: int):
    return account_repository.delete_account(db, account_id)