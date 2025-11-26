from pydantic import BaseModel
from typing import Union,Optional
from datetime import datetime


class CategoryCreation(BaseModel):
    name:str
    # user_id:int

class CategoryResponse(BaseModel):
    id:int
    user_id:int
    name:str

class TaskCreation(BaseModel):
    task_name:str
    description:str
    due_date:datetime
    category_id:int

class TaskResponse(BaseModel):
    id:int
    task_name:str
    description:str
    due_date:datetime
    category_id:int

class TaskUpdate(BaseModel):
    id:int
    task_name:Optional[str]=None
    description:Optional[str]=None
    due_date:Optional[datetime]=None
    category_id:Optional[int]=None
