from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import (sessionmaker, relationship, scoped_session)
from sqlalchemy.ext.declarative import declarative_base

sys.dont_write_bytecode = True

# setting db connection
url = "mysql+pymysql://root:root@localhost:3306/fastapi?charset=utf8"
engine = create_engine(url, echo=False, pool_recycle=10)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_new_session():
    return scoped_session(sessionmaker(autocommit=False, autoflush=True, expire_on_commit=False, bind=engine))
