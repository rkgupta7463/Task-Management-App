from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import schemas,models
from db.database import SessionLocal, engine
from contextlib import asynccontextmanager
from utils.init_db import create_tables
from router.auth import authRouter

@asynccontextmanager
async def lifespan(app:FastAPI):
    ## initliaze the DB to start
    print("DB's Tables getting created!")
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter,tags=["Auth"],prefix='/auth')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1️⃣ Create User
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 2️⃣ Read All Users
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# 3️⃣ Read Single User
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 4️⃣ Update User
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, updated_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
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
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
