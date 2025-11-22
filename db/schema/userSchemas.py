# schemas.py
from pydantic import BaseModel,EmailStr
from typing import Union

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password:str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password:str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    # password:str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr
    password:str

    class Config:
        orm_mode = True

class UserInLogin(BaseModel):
    email:EmailStr
    password:str

class UserWithToken(BaseModel):
    token:str
