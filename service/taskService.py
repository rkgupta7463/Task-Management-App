from db.repository.categoryRepo import CategoryRepo
from db.schema.taskSchema import TaskCreation,TaskResponse,TaskUpdate,CategoryCreation,CategoryResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.taskModel import Task,Category


class TaskService:
    def __init__(self,session:Session):
        self.__categoryRepository=CategoryRepo(session=session)

    def create_category(self,category_date:CategoryCreation)->CategoryResponse:
        return self.__categoryRepository.create_category(category_data=category_date)

    def get_all_category(self)->CategoryResponse:
        categories=self.__categoryRepository.get_category_all()
        if categories:
            return {"status":True,"message":"Records fetched!","data":categories}
        return {"status":False,"message":"No record found!","data":""}
    
    def get_category_by_name(self,cat_name)->CategoryResponse:
        category=self.__categoryRepository.get_category_by_name(cat_name=cat_name)
        if category:
            return {"status":True,"message":"Records fetched!","data":category}
        return {"status":False,"message":"No record found!","data":None}