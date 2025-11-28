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

    def get_task_all(self,user_id:int)->Task:
        tasks=self.session.query(Task).filter_by(user_id=user_id).all()
        return tasks

    def get_task_by_id(self,task_id:int,user_id:int)->Task:
        tasks=self.session.query(Task).filter_by(id=task_id,user_id=user_id).first()
        return tasks

    def get_task_by_name(self, task_name: str,user_id:int) -> Task:
        return (
            self.session.query(Task)
            .filter(Task.task_name.ilike(f"%{task_name}%")).filter_by(user_id=user_id)
            .all()
        )
