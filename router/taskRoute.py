from fastapi import APIRouter,Depends
from db.schema.taskSchema import TaskCreation,TaskResponse,TaskUpdate
from db.database import get_db
from sqlalchemy.orm import Session
from service.catService import CategoryService
from utils.protectedRoute import get_current_user
from db.schema.userSchemas import UserResponse


taskRouter=APIRouter()

@taskRouter.post('/add')
def create_task(task_data:TaskCreation,session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    try:
        return CategoryService(session=session).create_category(category_date=task_data)
    except Exception as e:
        print("Expection error: ",e)
        return {"status":True,"message":f"something went wrong! error: {e}"}

@taskRouter.get('/')
def get_all_task(session:Session=Depends(get_db)):
    return CategoryService(session=session).get_all_category()
