# Day 05 – Routers, Middleware, Error Handling & Testing

This project demonstrates how to organize FastAPI applications using routers, implement middleware, configure CORS, handle exceptions, execute background tasks, manage application lifespan events, and write automated API tests using pytest and TestClient.

---

## Topics Covered

- APIRouter
- Route prefixes and tags
- include_router()
- Custom HTTP middleware
- Request and response logging
- CORS (Cross-Origin Resource Sharing)
- Global exception handlers
- HTTPException handling
- Background tasks
- Lifespan events
- Automated API testing with pytest
- FastAPI TestClient

---

## Project Structure

```text
Day_05_Router_Middleware_Testing/
│
├── question_1/
│   ├── main.py
│   └── routers/
│       ├── users.py
│       └── auth.py
│
├── question_2/
│   └── main.py
│
├── question_3/
│   └── main.py
│
├── question_4/
│   └── main.py
│
├── question_5/
│   └── main.py
│
├── question_6/
│   ├── main.py
│   ├── tests/
│       └── test_users.py
│   
│
├── practice.py
└── README.md
```

---

## Practice Questions Implemented

### 1. APIRouter

- Split routes into separate router files
- Created:
  - `routers/users.py`
  - `routers/auth.py`
- Registered routers using `include_router()`
- Used route prefixes and tags for better organization

---

### 2. Middleware

Implemented custom HTTP middleware that logs:

- Request method
- Request path
- Response status code

Example output

```text
Request: GET /users
Response Status Code: 200
```

---

### 3. CORS Configuration

Configured `CORSMiddleware` to allow requests only from

```
http://localhost:3000
```

Configuration includes:

- Allowed origins
- Allowed methods
- Allowed headers
- Credentials support

---

### 4. Global Exception Handler

Implemented a global handler for `HTTPException`.

Custom error response format

```json
{
    "error": true,
    "detail": "User not found",
    "status": 404
}
```

---

### 5. Background Tasks

Implemented background task support using `BackgroundTasks`.

After creating a user, a background task simulates sending a welcome email by printing a message to the console without delaying the API response.

---

### 6. Lifespan Events

Implemented application lifespan events using `@asynccontextmanager`.

Startup

```text
Application Started
```

Shutdown

```text
Application Stopped
```

This demonstrates how startup and shutdown logic can be managed for resources such as database connections, caches, or machine learning models.

---

### 7. API Testing

Implemented automated API tests using `pytest` and `TestClient`.

Tests include:

- Successful user creation
- Duplicate email conflict (409)
- Protected route authentication

Run tests

```bash
pytest
```

or

```bash
python -m pytest -v
```

---

## API Endpoints

### Users

**POST**

```
/users
```

Creates a new user.

Returns

```json
{
    "message": "User created successfully"
}
```

---

### Profile

**GET**

```
/profile
```

Protected endpoint requiring an Authorization header.

Returns

```json
{
    "message": "Welcome"
}
```

Unauthorized requests return

```json
{
    "detail": "Unauthorized"
}
```

---

## Concepts Demonstrated

- Modular API design using routers
- Middleware execution before and after requests
- Cross-Origin Resource Sharing (CORS)
- Centralized exception handling
- Background task execution
- Application startup and shutdown events
- Automated API testing
- Request validation using Pydantic

---

## Learning Outcomes

By completing this project, I learned how to:

- Organize FastAPI projects using routers
- Build reusable and maintainable APIs
- Log incoming requests with middleware
- Configure secure CORS policies
- Customize API error responses
- Execute background tasks asynchronously
- Manage application startup and shutdown events
- Write automated tests using pytest and TestClient
- Verify API responses and status codes through testing

---