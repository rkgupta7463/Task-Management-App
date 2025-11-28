from fastapi import APIRouter,Depends
from db.schema.taskSchema import TaskCreation,TaskResponse,TaskUpdate
from db.database import get_db
from sqlalchemy.orm import Session
from service.taskService import TaskService
from utils.protectedRoute import get_current_user
from db.schema.userSchemas import UserResponse


taskRouter=APIRouter()

@taskRouter.post('/add')
def create_task(task_data:TaskCreation,session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    try:
        return TaskService(session=session).create_task(task_data=task_data,user_id=user.id)
    except Exception as e:
        print("Expection error: ",e)
        return {"status":True,"message":f"something went wrong! error: {e}"}

@taskRouter.get('/all')
def get_all_task(session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    return TaskService(session=session).get_all_tasks(user_id=user.id)

@taskRouter.get('/by')
def get_all_task(task_name,session:Session=Depends(get_db),user:UserResponse=Depends(get_current_user)):
    return TaskService(session=session).get_task_by_name(task_name=task_name,user_id=user.id)




