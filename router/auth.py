from fastapi import APIRouter
from db.schemas import UserInLogin,UserWithToken,UserCreate

authRouter=APIRouter()

@authRouter.post('/login')
def login(loginDetail:UserInLogin):
    return {"status":True,"message":"Logged in successfully!","data":loginDetail}

@authRouter.post('/signup')
def signup(signupDetail:UserCreate):
    return {"status":True,"message":"Registered successfully!","data":signupDetail}