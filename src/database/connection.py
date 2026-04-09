from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # atau sesuai punya kamu

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

<<<<<<< HEAD
def get_db(): 
    with Session(engine) as session:
        yield session
=======
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
>>>>>>> 9b045c51bb768bbd250802c96013b7a3548b878c
