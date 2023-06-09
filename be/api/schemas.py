from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


class UserBase(BaseModel):
    email: str



class UserCreate(UserBase):
    login_id: str
    password: str
    


class User(UserBase):
    id: int
    

    class Config:
        orm_mode = True
