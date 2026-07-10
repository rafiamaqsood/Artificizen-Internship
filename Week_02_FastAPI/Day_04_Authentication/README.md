# Day 04 – Authentication & Security

This project demonstrates authentication and authorization in FastAPI using JWT tokens, OAuth2 password flow, password hashing with Passlib, PostgreSQL, and role-based access control.

---

## Topics Covered

- Password hashing using Passlib (bcrypt)
- Password verification
- OAuth2 Password Flow
- JWT Authentication
- Token generation and validation
- Protected routes
- Current user dependency
- Role-based authorization
- Environment variables with python-dotenv
- PostgreSQL integration using SQLAlchemy

---

## Project Structure

```
Day_04_Authentication/
│
├── main.py
├── auth.py
├── security.py
├── database.py
├── models.py
├── config.py
├── test_security.py
├── requirements.txt
├── .env
└── README.md
```

---

## Technologies Used

- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- Passlib (bcrypt)
- Python-Jose
- Python-Dotenv
- Uvicorn

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql://postgres:your_password@localhost/fastapi_db

SECRET_KEY=

ALGORITHM=

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run the Application

```bash
python -m uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Register User

**POST**

```
/auth/register
```

Request

```json
{
    "username": "rafia",
    "password": "rafia123"
}
```

---

### Login

**POST**

```
/auth/token
```

Uses OAuth2PasswordRequestForm.

Returns

```json
{
    "access_token": "...",
    "token_type": "bearer"
}
```

---

### Current User

**GET**

```
/users/me
```

Requires

```
Authorization: Bearer <access_token>
```

Returns the authenticated user's information.

---

### Delete User (Admin Only)

**DELETE**

```
/users/{id}
```

Protected by the `require_admin` dependency.

- Admin → User deleted
- Non-admin → 403 Forbidden

---

## Authentication Workflow

1. Register a new user.
2. Password is hashed before being stored.
3. Login using username and password.
4. Receive a JWT access token.
5. Pass the token in the Authorization header.
6. Access protected endpoints.
7. Admin-only routes verify the user's role before allowing access.

---

## Practice Questions Implemented

### 1. Password Hashing

- Implemented `hash_password()`
- Implemented `verify_password()`
- Tested using `test_security.py`

---

### 2. User Registration

- Accepts username and password
- Checks duplicate usernames
- Hashes password
- Stores user in PostgreSQL

---

### 3. JWT Login

- Uses `OAuth2PasswordRequestForm`
- Verifies credentials
- Generates signed JWT
- Returns Bearer token

---

### 4. Current User Dependency

- Reads Authorization header
- Decodes JWT
- Returns authenticated user
- Raises 401 for invalid tokens

---

### 5. Protected Route

Protected

```
GET /users/me
```

Only authenticated users can access it.

---

### 6. Role-Based Authorization

- Added `role` column to the user model
- Implemented `require_admin`
- Protected

```
DELETE /users/{id}
```

Only administrators can perform delete operations.

---

## Security Features

- Password hashing with bcrypt
- JWT authentication
- OAuth2 Password Flow
- Environment variables
- Token expiration
- Protected routes
- Role-based authorization
- Plaintext passwords are never stored

---
