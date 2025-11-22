# models.py
from sqlalchemy import Column, Integer, String,DateTime,ForeignKeyConstraint
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)

    # Reverse relation → A category has many tasks
    tasks = relationship("Task", back_populates="category")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(150), index=True)
    description = Column(String(250))

    # New DateTime fields
    start_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)

    # Foreign key
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Relationship
    category = relationship("Category", back_populates="tasks")
    
