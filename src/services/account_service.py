from sqlalchemy.orm import Session
from src.repositories import account_repository
from src.database.schema.account import Account

def get_accounts(db: Session):
    return account_repository.get_all_accounts(db)

def create_account(db: Session, account_data):
    account = Account(**account_data.dict())
    return account_repository.create_account(db, account)