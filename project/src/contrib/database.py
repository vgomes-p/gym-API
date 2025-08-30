from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://workout:workout@localhost/workout"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()