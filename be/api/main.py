from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import handle_db
import models
from databases import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# select user list
@app.get(path="/api/users")
async def get_list_user():
    result = handle_db.select_all_user()
    return {
        "status": "OK",
        "data": result
    }

# create user


@app.post(path="/api/users")
async def post_user(user_password: str, user_mail: str):
    result = handle_db.create_user(user_password, user_mail)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# select user


@app.get(path="/api/users/{user_id}")
async def get_user(user_id: str):
    result = handle_db.select_user(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# update user


@app.put(path="/api/users/{user_id}")
async def put_user(user_mail: str,  user_password: str, user_id: str):
    result = handle_db.update_user(user_id, user_mail, user_password)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# delete user


@app.delete(path="/api/users/{user_id}")
async def delete_user(user_id: str):
    result = handle_db.delete_user(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
