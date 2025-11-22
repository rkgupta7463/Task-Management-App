from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schema import userSchemas
from db.database import SessionLocal, engine
from contextlib import asynccontextmanager
from db.models import userModel
from utils.init_db import create_tables
from router.auth import authRouter
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


@app.get("/get_current_user")
def current_user(user:UserResponse=Depends(get_current_user)):
    return user

# 1️⃣ Create User
@app.post("/users/", response_model=userSchemas.UserResponse)
def create_user(user: userSchemas.UserCreate, db: Session = Depends(get_db)):
    db_user = userModel.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 2️⃣ Read All Users
@app.get("/users/", response_model=list[userSchemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(userModel.User).all()


# 3️⃣ Read Single User
@app.get("/users/{user_id}", response_model=userSchemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 4️⃣ Update User
@app.put("/users/{user_id}", response_model=userSchemas.UserResponse)
def update_user(user_id: int, updated_data: userSchemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_data.name
    user.email = updated_data.email

    db.commit()
    db.refresh(user)
    return user


# 5️⃣ Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
