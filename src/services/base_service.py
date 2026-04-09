from src.repository.base_repository import update_data, delete_data

def update_entity(db, model, id, data):
    return update_data(db, model, id, data)

def delete_entity(db, model, id):
    return delete_data(db, model, id)