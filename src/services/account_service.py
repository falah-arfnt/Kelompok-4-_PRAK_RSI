from src.repositories import account_repository


def get_all_accounts(db):
    return account_repository.get_all(db)


def get_account_by_id(db, account_id: int):
    return account_repository.get_by_id(db, account_id)


def create_account(db, data):
    return account_repository.create(db, data)


def update_account(db, account_id: int, data):
    return account_repository.update(db, account_id, data)


def delete_account(db, account_id: int):
    return account_repository.delete(db, account_id)