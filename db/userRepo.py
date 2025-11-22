from .base import BaseRepository
from .models import User
from .schemas import UserCreate

class UserAuthRepo(BaseRepository):
    def create_user(self,user_data:UserCreate):
        newUser=User(user_data.model_dump(exclude_none=True))# if we want to restrict that `none` value should not pass in model_dump() function so use `User(user_data.model_dump(exclude_none=True))`
        self.session.add(newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)

        return newUser

    def user_exist_by_email(self,email:str)->bool:
        user=self.session.query(User).filter_by(email=email).first()
        return bool(user)

    def get_user_by_email(self,email:str)->User:
        user=self.session.query(User).filter_by(email=email).first()
        return user
    
    def get_user_by_email(self,user_id:int)->User:
        user=self.session.query(User).filter_by(id=user_id).first()
        return user
