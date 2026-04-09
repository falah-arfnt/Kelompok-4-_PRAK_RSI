from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import account_controller
from src.database.schema.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])

# GET
@router.get("/", response_model=list[AccountResponse])
def get_accounts(db: Session = Depends(get_db)):
    return account_controller.get_accounts(db)

# POST
@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return account_controller.create_account(db, account)

# PUT
@router.put("/{id}", response_model=AccountResponse)
def update_account(id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    return account_controller.update_account(db, id, account)

# DELETE
@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    return account_controller.delete_account(db, id)