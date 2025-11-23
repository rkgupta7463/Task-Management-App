from fastapi import APIRouter,Depends
from db.schema.taskSchema import CategoryCreation,CategoryResponse,TaskCreation,TaskResponse,TaskUpdate
from db.database import get_db
from sqlalchemy.orm import Session
from service.taskService import CategoryService

categoryRouter=APIRouter()

@categoryRouter.post('/add')
def create_category(category_data:CategoryCreation,session:Session=Depends(get_db)):
    try:
        return CategoryService(session=session).create_category(category_date=category_data)
    except Exception as e:
        print("Expection error: ",e)
        return {"status":True,"message":f"something went wrong! error: {e}"}

@categoryRouter.get('/all')
def get_all_task(session:Session=Depends(get_db)):
    return CategoryService(session=session).get_all_category()

@categoryRouter.get('/by')
def get_all_task(cat_name,session:Session=Depends(get_db)):
    return CategoryService(session=session).get_category_by_name(cat_name=cat_name)


