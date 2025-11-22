from db.repository.userRepo import UserAuthRepo
from db.schema.userSchemas import UserCreate,UserResponse,UserInLogin,UserWithToken
from security.hashHelper import HashHelper
from security.authHandler import AuthHandler
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.userModel import User

class UserService:
    def __init__(self,session:Session):
        self.__userRepository=UserAuthRepo(session=session)

    def signup(self,user_data:UserCreate) ->UserResponse:
        if self.__userRepository.user_exist_by_email(email=user_data.email):
            raise HTTPException(status_code=400,detail="Email ID is already exist! Please Login!")
        
        hash_password=HashHelper.get_password_hash(plain_password=user_data.password)

        user_data.password=hash_password
        return self.__userRepository.create_user(user_data=user_data)
    
    def login(self,user_data:UserInLogin)->UserWithToken:
        if not self.__userRepository.user_exist_by_email(email=user_data.email):
            raise HTTPException(status_code=400,detail="Email ID doesn't exist! Please Register!")
        
        user=self.__userRepository.get_user_by_email(email=user_data.email)
        if HashHelper.verify_password(plain_password=user_data.password,hashed_password=user.password):
            token=AuthHandler.sign_jwt(user_id=user.id)
            if token:
                return UserWithToken(token=token)
            raise HTTPException(status_code=500,detail="Unable to process the request.")
        else:
            raise HTTPException(status_code=400,detail="Please check your Credentials!")

    def get_user_by_user_id(self,user_id:int)->User:
        user = self.__userRepository.get_user_by_user_id(user_id=user_id)
        if user:
            return user    
        else:
            raise HTTPException(status_code=400,detail="User is not found!")
