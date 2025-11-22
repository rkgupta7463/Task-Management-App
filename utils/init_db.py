from db.database import Base,engine
from db.models.userModel import *

def create_tables():
    Base.metadata.create_all(bind=engine)
