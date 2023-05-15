# -*- encoding: utf-8 -*-
import datetime
import uuid
import sys
from sqlalchemy import VARCHAR, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from databases import Base, engine

sys.dont_write_bytecode = True

base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.created_at = now_time
        self.updated_at = now_time

if __name__ == "__main__":
    Base.metadata.create_all(engine)

