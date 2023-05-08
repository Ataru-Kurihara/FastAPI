from dotenv import load_dotenv
load_dotenv()

import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")

