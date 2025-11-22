# models.py
from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    __tablename__ = "users"  # Table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True)
    email = Column(String(22), unique=True, index=True)
    password=Column(String(250))
    
