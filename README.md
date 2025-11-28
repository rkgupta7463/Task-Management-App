# Task Manager API – FastAPI

A fully functional **Task Manager REST API** built using **FastAPI**, featuring:

✅ JWT Authentication  
✅ User Signup & Login  
✅ Get Current Authenticated User  
✅ CRUD Operations for **Users**, **Tasks**, and **Categories**  
✅ Modular Project Structure (Routers, Services, Security)  
✅ SQLAlchemy ORM + Alembic Migrations  
✅ Auto-generated Swagger & ReDoc documentation  

---

## Features

### Authentication
- User Signup  
- User Login (JWT-based)  
- Get current authenticated user  
- Protected routes 

### User Management
- Create user  
- Get all users  
- Get user by ID  
- Update user  
- Delete user  

### Task Management
- Create Task  
- Get All Tasks  
- Get Task by ID  
- Update Task  
- Delete Task  

### Category Management
- Create Category  
- Get All Categories  
- Delete Category  

### Documentation
- Swagger UI → /docs
- ReDoc → /redoc

---

## Project Structure

```
FASTAPI_PROJ/
│── alembic/
│── db/
│── env/
│── router/
│   ├── auth_router.py
│   ├── task_router.py
│   └── user_router.py
│── security/
│   └── authHandler.py
|   |__ hashHelper.py
│── service/
│   ├── task_service.py
│   ├── user_service.py
│   └── category_service.py
│── utils/
│── main.py
│── requirements.txt
│── alembic.ini
│── test.db
│── README.md
```

---

## Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/yourname/taskmanager-fastapi.git
cd taskmanager-fastapi
```

### 2. Create a virtual environment
```
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate   # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run Alembic migrations
```
alembic upgrade head
```

### 5. Start the FastAPI server
```
uvicorn main:app --reload
```

---

## API Endpoints

### Authentication
- POST /auth/signup  
- POST /auth/login  

### Users
- GET /users/
- GET /users/{user_id}
- PUT /users/{user_id}
- DELETE /users/{user_id}

### Tasks
- POST /task/add
- GET /task/all
- GET /tasks/by?task_name=<task_name>
- GET /task/{task_id}
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}

### Categories
- POST /category/add
- GET /category/all
- GET /category/by?cat_name=<cat_name>
- GET /category/{category_id}
- DELETE /categories/{category_id}

---

## Documentation URLs
- Swagger: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

---

## License
MIT License
