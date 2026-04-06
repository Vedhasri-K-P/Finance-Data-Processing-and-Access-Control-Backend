# Finance-Data-Processing-and-Access-Control-Backend

# 💰 Finance Dashboard Backend

## 🚀 Overview

This project is a backend system built using FastAPI for managing financial records with role-based access control and JWT authentication. It supports user management, secure login, CRUD operations on financial data, and dashboard analytics.

---

## ✨ Features

### 🔐 Authentication & Authorization

* JWT-based authentication
* Secure password hashing using bcrypt
* Role-Based Access Control (RBAC)

  * Admin → Full access
  * Analyst → Read + insights
  * Viewer → View only

---

### 👤 User Management

* Create users
* Assign roles
* Prevent duplicate registrations

---

### 💰 Financial Records

* Create records (income/expense)
* View records
* Delete records
* Fields:

  * Amount
  * Type (income/expense)
  * Category
  * Date
  * Notes

---

### 📊 Dashboard Analytics

* Total income
* Total expenses
* Net balance

---

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)

---

## 🔐 Authentication Flow

1. Create user via `/users`
2. Login via `/login`
3. Copy JWT token
4. Click **Authorize 🔒** in Swagger
5. Use token:
   Bearer <your_token>

---

## 📡 API Endpoints

### 👤 Users

* `POST /users` → Create user
* `GET /users` → Get all users

### 🔐 Auth

* `POST /login` → Get JWT token

### 💰 Records

* `POST /records` → Create record
* `GET /records` → Get records
* `DELETE /records/{id}` → Delete record

### 📊 Dashboard

* `GET /dashboard/summary` → Get financial summary

---

## ▶️ Run the Project

### 1. Clone repository

```bash
git clone <your-repo-link>
cd finance-backend
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run server

```bash
uvicorn app.main:app --reload
```

### 5. Open Swagger

http://127.0.0.1:8000/docs

---

## 📌 Assumptions

* Roles are predefined (admin, analyst, viewer)
* SQLite used for simplicity
* JWT used for authentication

---

## 🧠 Design Approach

The backend is structured into modular components:

* Models → Database structure
* Routes → API endpoints
* Schemas → Data validation
* Utils → Authentication & role logic

This ensures clean separation of concerns and maintainability.

---

## ⚠️ Notes

* Passwords are securely hashed
* JWT tokens are required for protected routes
* Proper error handling and validation implemented

---

## 📈 Future Improvements (Optional)

* Category-wise analytics
* Filters (date, category)
* Pagination
* Unit testing

---

## 🎯 Conclusion

This project demonstrates backend architecture, API design, authentication, authorization, and data processing suitable for real-world financial applications.
