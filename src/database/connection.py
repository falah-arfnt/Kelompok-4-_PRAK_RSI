from sqlmodel import create_engine, Session

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/crud_db"

engine = create_engine(DATABASE_URL, echo=True)

def get_db(): 
    with Session(engine) as session:
        yield session