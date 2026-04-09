from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import account_controller
from src.dto.account_dto import AccountCreate

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    return account_controller.get_accounts(db)

@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return account_controller.create_account(db, account)