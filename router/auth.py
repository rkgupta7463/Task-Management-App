from fastapi import APIRouter,Depends
from db.schema.userSchemas import UserInLogin,UserWithToken,UserCreate,UserResponse
from db.database import get_db
from sqlalchemy.orm import Session
from service.userService import UserService

authRouter=APIRouter()

@authRouter.post('/login',status_code=200,response_model=UserWithToken)
def login(loginDetail:UserInLogin,session:Session=Depends((get_db))):
    try:
        return UserService(session=session).login(user_data=loginDetail)
    except Exception as e: 
        print("error: ",e)
        return {"status":True,"message":f"{e}","data":''}

@authRouter.post('/signup',status_code=201,response_model=UserResponse)
def signup(signupDetail:UserCreate,session:Session=Depends(get_db)):
    try:
        return UserService(session=session).signup(user_data=signupDetail)
    except Exception as e:
        print("error:",e)
        return {"status":True,"message":f"{e}","data":""}