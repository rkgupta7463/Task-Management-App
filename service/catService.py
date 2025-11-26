from db.repository.categoryRepo import CategoryRepo
from db.schema.taskSchema import TaskCreation,TaskResponse,TaskUpdate,CategoryCreation,CategoryResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.taskModel import Task,Category


class CategoryService:
    def __init__(self,session:Session):
        self.__categoryRepository=CategoryRepo(session=session)

    def create_category(self,user_id,category_date:CategoryCreation)->CategoryResponse:
        return self.__categoryRepository.create_category(category_data=category_date,user_id=user_id)

    def get_all_category(self,user_id)->CategoryResponse:
        categories=self.__categoryRepository.get_category_all(user_id=user_id)
        if categories:
            return {"status":True,"message":"Records fetched!","data":categories}
        return {"status":False,"message":"No record found!","data":""}
    
    def get_category_by_name(self,cat_name,user_id)->CategoryResponse:
        category=self.__categoryRepository.get_category_by_name(cat_name=cat_name,user_id=user_id)
        if category:
            return {"status":True,"message":"Records fetched!","data":category}
        return {"status":False,"message":"No record found!","data":None}