🚀 User Profile Management System

A full-stack web application built using Next.js (Frontend), FastAPI (Backend), and PostgreSQL (Database).
This project allows users to Register, Login, View Profile, and Update Profile.

It demonstrates end-to-end full-stack development, including form handling, REST APIs, database operations, and clean UI design.

📌 Features
✅ User Registration

Users can create an account with Name, Email, and Password.

Passwords are securely hashed before storing in the database.

✅ User Login

Users can log in with email and password.

Validates user authentication.

✅ View Profile

Fetches profile data based on User ID.

Displays name, email, created time, updated time.

✅ Update Profile

Allows editing name, email, and password.

Saves updates to PostgreSQL database.

✅ Fully Responsive UI

Built using Next.js + CSS.

Background image support.

✅ REST APIs

Clean and well-structured FastAPI endpoints.

Swagger documentation included.

🛠️ Tech Stack
Frontend

Next.js 14

React

CSS Modules

Axios

Backend

FastAPI

Pydantic

SQLAlchemy ORM

Uvicorn

Database

PostgreSQL

pgAdmin 4 (Optional GUI)

📁 Project Structure
user-profile-management/
│
├── backend/
│   ├── main.py                # All API routes (register, login, profile, update)
│   ├── database.py            # Database connection + session
│   ├── models.py              # SQLAlchemy Models (User table)
│   ├── schemas.py             # Pydantic schemas for validation
│   ├── requirements.txt       # Backend dependencies
│   └── .env                   # PostgreSQL connection URL
│
└── frontend/
    ├── app/
    │   ├── globals.css        # Global CSS + background image
    │   ├── page.tsx           # Home screen
    │   ├── register/
    │   │   └── page.tsx       # Register UI
    │   ├── login/
    │   │   └── page.tsx       # Login UI
    │   ├── profile/
    │   │   └── page.tsx       # Fetch Profile
    │   └── update-profile/
    │       └── page.tsx       # Update Profile UI
    ├── package.json
    └── next.config.js

⚙️ How to Run the Project
1️⃣ Setup PostgreSQL Database

Install PostgreSQL and pgAdmin.

Create a new database named:

user_management


(Optional) If table not created automatically, run:

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

2️⃣ Setup Backend (FastAPI)
Step 1 — Move to backend folder
cd backend

Step 2 — Install requirements
pip install -r requirements.txt

Step 3 — Run FastAPI server
uvicorn main:app --reload

Backend will run at:

API Root: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

3️⃣ Setup Frontend (Next.js)
Step 1 — Move to frontend
cd frontend

Step 2 — Install npm packages
npm install

Step 3 — Run project
npm run dev

Frontend available at:

👉 http://localhost:3000

🔗 API Endpoints
POST /register

Create a new user.

POST /login

Authenticate user.

GET /profile/{id}

Fetch user profile by ID.

PUT /update-profile/{id}

Update name, email, password.

Screenshot

🎯 Project Summary

The User Profile Management System demonstrates:

Full CRUD operations

Secure password hashing

Real database storage with PostgreSQL

Clean REST API design

Fully functional UI built with Next.js

Real-time user interaction

Integration between frontend, backend, and database

This project is ideal for interviews, college submissions, hackathons, and portfolio showcasing.

✅ Conclusion

This full-stack system provides a complete flow of a real-world user management feature. It covers everything from frontend UI, backend API logic, database operations, security implementations, and deployment-ready structure.
