# Day 01 FastAPI Basics & Setup
## Overview

This folder contains my solutions and practice exercises completed during **Day 01** of **Week 02** of the internship training plan. The focus of this day was learning the fundamentals of **FastAPI**, understanding how to build REST APIs, handle requests and responses, use path and query parameters, work with HTTP status codes, and explore the automatically generated API documentation.

---

## Topics Covered

### Introduction to FastAPI

* What is FastAPI
* Why FastAPI is used
* Async-first framework
* Automatic API documentation
* Pydantic integration

### Environment Setup

* Virtual Environment (`venv`)
* Installing FastAPI
* Installing Uvicorn
* Running the development server

### FastAPI Application

* Creating a FastAPI application
* `FastAPI()` instance
* Route decorators
* First API endpoint

### Path Parameters

* Dynamic URL parameters
* Type annotations
* Automatic validation

### Query Parameters

* Optional query parameters
* Default values
* Pagination using `skip` and `limit`

### HTTP Methods

* `GET`
* `POST`

### Status Codes & Exceptions

* Returning custom status codes
* `HTTPException`
* `status` module

### Interactive API Documentation

* Swagger UI (`/docs`)
* ReDoc (`/redoc`)
* Testing endpoints directly from the browser

---

## Practice Questions Implemented

### 1. Hello Artificizen API

Created a basic FastAPI application with a root endpoint that returns a welcome message.

**Concepts Used**

* FastAPI Application
* GET Request
* JSON Response

File:

```text
main.py
```

---

### 2. User Path Parameter

Created a dynamic endpoint that accepts a user ID as a path parameter and returns it as an integer. Also observed FastAPI's automatic validation when passing an invalid value.

**Concepts Used**

* Path Parameters
* Type Hints
* Automatic Validation

File:

```text
main.py
```

---

### 3. Fake Pagination API

Created an endpoint that returns a fake list of items using optional query parameters `skip` and `limit`.

**Concepts Used**

* Query Parameters
* Default Values
* List Slicing
* Pagination

File:

```text
main.py
```

---

### 4. Custom HTTP Exception

Implemented custom error handling using `HTTPException` to return a **404 Not Found** response when a requested user ID is greater than `100`.

**Concepts Used**

* HTTPException
* Status Codes
* Conditional Logic

File:

```text
main.py
```

---

### 5. POST Endpoint with Status Code

Created a `POST /ping` endpoint that returns a **201 Created** response along with a JSON message.

**Concepts Used**

* POST Request
* HTTP Status Codes
* `status.HTTP_201_CREATED`

File:

```text
main.py
```

---

### 6. API Documentation

Explored FastAPI's automatically generated API documentation using Swagger UI and ReDoc. Tested all implemented endpoints directly from the browser without writing any client code.

**Concepts Used**

* Swagger UI
* ReDoc
* API Testing

---

## Folder Structure

```text
Day_01_FastAPI_Basics/
│
├── main.py
└── README.md
```

---

## How to Run

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
venv\Scripts\Activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn[standard]
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```
