from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.controllers import account_controller
<<<<<<< HEAD
from src.dto.account_dto import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])

=======
from src.database.schema.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])

# GET
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
@router.get("/", response_model=list[AccountResponse])
def get_accounts(db: Session = Depends(get_db)):
    return account_controller.get_accounts(db)

<<<<<<< HEAD
@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    account = account_controller.get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

=======
# POST
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return account_controller.create_account(db, account)

<<<<<<< HEAD
@router.put("/{account_id}", response_model=AccountResponse)
def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = account_controller.get_account_by_id(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account_controller.update_account(db, account_id, account)

@router.patch("/{account_id}", response_model=AccountResponse)
def patch_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = account_controller.get_account_by_id(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account_controller.update_account(db, account_id, account)

@router.delete("/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    account = account_controller.get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    account_controller.delete_account(db, account_id)
    return {"message": "Account deleted successfully"}
=======
# PUT
@router.put("/{id}", response_model=AccountResponse)
def update_account(id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    return account_controller.update_account(db, id, account)

# DELETE
@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    return account_controller.delete_account(db, id)
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
