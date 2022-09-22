from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    passwd: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True