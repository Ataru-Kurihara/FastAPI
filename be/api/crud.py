# from sqlalchemy.orm import Session
# import models
# import schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_login_id(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User.login_id).offset(skip).limit(limit).all()

# def get_user_by_id(db: Session, login_id: str):
#     return db.query(models.User).filter(models.User.login_id == login_id).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: models.User):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(login_id=user.login_id, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# # def get_items(db: Session, skip: int = 0, limit: int = 100):
# #     return db.query(models.Item).offset(skip).limit(limit).all()


# # def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
# #     db_item = models.Item(**item.dict(), owner_id=user_id)
# #     db.add(db_item)
# #     db.commit()
# #     db.refresh(db_item)
# #     return db_item
