from fastapi import APIRouter,Depends
from db.schema.taskSchema import CategoryCreation,CategoryResponse,TaskCreation,TaskResponse,TaskUpdate
from db.database import get_db
from sqlalchemy.orm import Session
from service.catService import CategoryService
from utils.protectedRoute import get_current_user
from db.schema.userSchemas import UserResponse

categoryRouter=APIRouter()

@categoryRouter.post('/add')
def create_category(category_data:CategoryCreation,session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    try:
        return CategoryService(session=session).create_category(category_date=category_data,user_id=user.id)
    except Exception as e:
        print("Expection error: ",e)
        return {"status":True,"message":f"something went wrong! error: {e}"}

@categoryRouter.get('/all')
def get_all_task(session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    return CategoryService(session=session).get_all_category(user_id=user.id)

@categoryRouter.get('/by')
def get_all_category(cat_name,session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    return CategoryService(session=session).get_category_by_name(cat_name=cat_name,user_id=user.id)


