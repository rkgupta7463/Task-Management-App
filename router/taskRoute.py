from fastapi import APIRouter,Depends
from db.schema.userSchemas import UserInLogin,UserWithToken,UserCreate,UserResponse
from db.database import get_db
from sqlalchemy.orm import Session
from service.userService import UserService


taskRouter=APIRouter()
