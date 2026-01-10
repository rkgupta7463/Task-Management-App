from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schema import userSchemas
from db.database import SessionLocal, engine
from contextlib import asynccontextmanager
from db.models import userModel
from utils.init_db import create_tables
from router.auth import authRouter
from router.usersRoute import create_user
from router.taskRoute import taskRouter
from router.categoryRoute import categoryRouter
from db.database import get_db
from utils.protectedRoute import get_current_user
from db.schema.userSchemas import UserResponse

@asynccontextmanager
async def lifespan(app:FastAPI):
    ## initliaze the DB to start
    print("DB's Tables getting created!")
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter,tags=["Auth"],prefix='/auth')
app.include_router(router=authRouter,tags=["user"],prefix='/user')
app.include_router(router=taskRouter,tags=["task"],prefix='/task')
app.include_router(router=categoryRouter,tags=["category"],prefix='/category')

