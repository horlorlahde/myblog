# from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from fastapi import Depends


SQLALCHEMY_DATABASE_URL = 'sqlite:///./mytable.db'

engine= create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False} )

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base= declarative_base()

# db_d = Annotated[Session, Depends()]
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

