from db.repository.taskRepo import TaskRepo
from db.schema.taskSchema import TaskCreation,TaskResponse,TaskUpdate,CategoryCreation,CategoryResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.taskModel import Task,Category


class TaskService:
    def __init__(self,session:Session):
        self.__taskRepository=TaskRepo(session=session)

    def create_task(self,user_id,task_data:TaskCreation)->TaskResponse:
        return self.__taskRepository.create_task(task_data=task_data,user_id=user_id)

    def get_all_tasks(self,user_id)->TaskResponse:
        tasks=self.__taskRepository.get_task_all(user_id=user_id)
        if tasks:
            return {"status":True,"message":"Records fetched!","data":tasks}
        return {"status":False,"message":"No record found!","data":""}
    
    def get_task_by_name(self,task_name,user_id)->CategoryResponse:
        tasks=self.__taskRepository.get_task_by_name(task_name=task_name,user_id=user_id)
        if tasks:
            return {"status":True,"message":"Records fetched!","data":tasks}
        return {"status":False,"message":"No record found!","data":None}