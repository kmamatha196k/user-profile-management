from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import psycopg2.extras
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# PostgreSQL Connection
try:
    connection = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print("Connected to PostgreSQL")
except Exception as e:
    print("PostgreSQL Error:", e)


# MongoDB Connection
try:
    mongo_client = MongoClient(os.getenv("MONGO_URL"))
    mongo_db = mongo_client[os.getenv("MONGO_DB")]
    mongo_collection = mongo_db[os.getenv("MONGO_COLLECTION")]
    print("Connected to MongoDB")
except Exception as e:
    print("MongoDB Error:", e)


# MODELS
class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


# ROUTES
@app.post("/register")
def register_user(data: UserRegister):
    try:
        # hash password
        hashed_password = pwd_context.hash(data.password)

        # INSERT into PostgreSQL
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (data.name, data.email, hashed_password),
        )
        connection.commit()

        # Save log into MongoDB
        mongo_collection.insert_one(
            {"name": data.name, "email": data.email, "action": "registered"}
        )

        return {"message": "User registered successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login")
def login(data: UserLogin):
    cursor.execute("SELECT * FROM users WHERE email=%s", (data.email,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not pwd_context.verify(data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect password")

    # Save login log to MongoDB
    mongo_collection.insert_one(
        {"email": data.email, "action": "login"}
    )

    return {"message": "Login successful", "user": user}


@app.get("/profile/{user_id}")
def get_profile(user_id: int):
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/profile/{user_id}")
def update_profile(user_id: int, data: UserRegister):
    try:
        hashed_password = pwd_context.hash(data.password)

        cursor.execute(
            "UPDATE users SET name=%s, email=%s, password=%s, updated_at=NOW() WHERE id=%s",
            (data.name, data.email, hashed_password, user_id),
        )
        connection.commit()
        return {"message": "Profile updated successfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))