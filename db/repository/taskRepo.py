from ..base import BaseRepository
from ..models.taskModel import Task
from ..schema.taskSchema import CategoryCreation,CategoryResponse,TaskCreation,TaskResponse

class TaskRepo(BaseRepository):
    def create_task(self,user_id,task_data:TaskCreation):
        newCategory=Task(**task_data.model_dump(exclude_none=True))# if we want to restrict that `none` value should not pass in model_dump() function so use `User(user_data.model_dump(exclude_none=True))`
        newCategory.user_id=user_id
        self.session.add(newCategory)
        self.session.commit()
        self.session.refresh(instance=newCategory)

        return newCategory

    def get_category_all(self,user_id:int)->Task:
        category=self.session.query(Task).filter_by(user_id=user_id).all()
        return category

    def get_category_by_id(self,cat_id:int,user_id:int)->Task:
        category=self.session.query(Task).filter_by(id=cat_id,user_id=user_id).first()
        return category

    def get_category_by_name(self, cat_name: str,user_id:int) -> Task:
        return (
            self.session.query(Task)
            .filter(Task.name.ilike(f"%{cat_name}%")).filter_by(user_id=user_id)
            .all()
        )
