# models.py
from sqlalchemy import Column, Integer, String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(150), index=True)
    email = Column(String(150), unique=True, index=True)
    phone_no=Column(String(14),unique=True,index=True)
    purpose=Column(String(255),nullable=True)
    password = Column(String(250))

    # User → Categories (one-to-many)
    categories = relationship("Category", back_populates="user")

    # User → Tasks (one-to-many)
    tasks = relationship("Task", back_populates="user")

    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow)



    
