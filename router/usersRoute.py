from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schema import userSchemas
from db.models import userModel
from db.database import get_db
from utils.protectedRoute import get_current_user
from db.schema.userSchemas import UserResponse

app=APIRouter()

@app.get("/get_current_user")
def current_user(user:UserResponse=Depends(get_current_user)):
    return user

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
