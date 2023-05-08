from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config


user = config.DB_USER
password = config.DB_PASSWORD
host = config.HOST
database = config.DATABASE
SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
