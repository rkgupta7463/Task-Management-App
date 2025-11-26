from ..base import BaseRepository
from ..models.taskModel import Category,Task
from ..schema.taskSchema import CategoryCreation,CategoryResponse,TaskCreation,TaskResponse

class CategoryRepo(BaseRepository):
    def create_category(self,user_id,category_data:CategoryCreation):
        newCategory=Category(**category_data.model_dump(exclude_none=True))# if we want to restrict that `none` value should not pass in model_dump() function so use `User(user_data.model_dump(exclude_none=True))`
        newCategory.user_id=user_id
        self.session.add(newCategory)
        self.session.commit()
        self.session.refresh(instance=newCategory)

        return newCategory

    def get_category_all(self,user_id:int)->Category:
        category=self.session.query(Category).filter_by(user_id=user_id).all()
        return category

    def get_category_by_id(self,cat_id:int,user_id:int)->Category:
        category=self.session.query(Category).filter_by(id=cat_id,user_id=user_id).first()
        return category

    def get_category_by_name(self, cat_name: str,user_id:int) -> Category:
        return (
            self.session.query(Category)
            .filter(Category.name.ilike(f"%{cat_name}%")).filter_by(user_id=user_id)
            .all()
        )
