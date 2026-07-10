# AI Engineer Internship – Artificizen

This repository contains my daily training tasks, exercises, and projects completed during my AI Engineer internship at Artificizen.

---

# Week 01 – Python Revision & OOP

## Day 01 – Python Fundamentals

### Topics Covered

* Variables & Data Types
* Operators
* String Formatting
* Conditionals
* Loops
* Input / Output

---

## Day 02 – Data Structures

### Topics Covered

* Lists
* Tuples
* Dictionaries
* Sets
* Strings

---

## Day 03 – Functions & Functional Tools

### Topics Covered

* Function Basics (`def`, parameters, return values)
* Default Arguments
* `*args` and `**kwargs`
* Lambda Functions
* `map()`
* `filter()`
* `zip()`
* `enumerate()`
* `sorted()` with `key`
* Local vs Global Scope
* `global` Keyword
* Recursion (Factorial & Fibonacci)
* Modules (`import`, `from ... import`, Custom Modules)

---

## Day 04 – Object-Oriented Programming (OOP) Part 1

### Topics Covered

* Classes & Objects
* `__init__()` Constructor and `self`
* Instance Variables vs Class Variables
* Instance Methods
* `@classmethod`
* `@staticmethod`
* Encapsulation (Public, Protected, Private)
* `@property`

---

## Day 05 – Object-Oriented Programming (OOP) Part 2 + Practical Python

### Topics Covered

* Inheritance (Single & Multiple)
* `super()`
* Polymorphism
* Method Overriding
* Duck Typing
* Abstraction (`abc` Module)
* Dunder (Magic) Methods
* Exception Handling
* File Handling
* JSON Handling
* Virtual Environments (`venv`)
* `pip`
* `requirements.txt`
* Basic Type Hints

---

# Week 01 Capstone Project

## Library Management System (CLI)

A command-line Library Management System developed using Python to apply all concepts learned during Week 1.

### Features

* Add Books
* Add Members
* Search Books

  * By ISBN
  * By Title
* Issue Books
* Return Books
* View All Books
* View All Members
* JSON Data Persistence
* Custom Exception Handling
* Input Validation
* Menu-Driven CLI

---

# Week 02 – FastAPI

## Day 01 – FastAPI Basics & Setup

### Topics Covered

* Introduction to FastAPI
* Virtual Environment Setup
* Installing FastAPI & Uvicorn
* Creating a FastAPI Application
* Running the Development Server
* Path Parameters
* Query Parameters
* HTTP Methods (GET, POST)
* HTTP Status Codes
* `HTTPException`
* Interactive API Documentation (Swagger UI & ReDoc)

---

## Day 02 – Pydantic Models & Request/Response Validation

### Topics Covered

* Pydantic `BaseModel`
* Request Body Validation
* Field Constraints using `Field()`
* Optional Fields & Default Values
* Nested Models
* Response Models (`response_model`)
* `@field_validator`
* `model_dump()`
* `ConfigDict(from_attributes=True)`
* Create vs Read Schema Pattern
* Advanced Pydantic Models
* `Annotated`
* `EmailStr`
* Strict Type Validation
* Collection Types (`List`, `Dict`)
* Custom Email Domain Validation

---

## Day 03 – Database Integration with SQLAlchemy

### Topics Covered

* SQLAlchemy Setup
* PostgreSQL Integration
* Database URL Configuration
* `create_engine()`
* `SessionLocal`
* `declarative_base()`
* SQLAlchemy Models
* CRUD Operations
* Dependency Injection using `Depends(get_db)`
* Pydantic Schemas
* SQLAlchemy Models vs Pydantic Schemas
* One-to-Many Relationships
* `ForeignKey`
* `relationship()`
* `back_populates`
* Alembic Setup
* Database Migrations
* Auto-generated Migration Files

---

## Day 04 – Authentication & Security

### Topics Covered

* Password Hashing with Passlib (`CryptContext`, `hash()`, `verify()`)
* OAuth2 Password Flow
* `OAuth2PasswordBearer`
* `OAuth2PasswordRequestForm`
* JWT Authentication using `python-jose`
* JWT Token Creation and Validation
* Access Token Expiration (`exp` Claim)
* User Registration with Hashed Passwords
* Login Endpoint (`/auth/token`)
* Protected Routes using Dependencies
* `get_current_user` Dependency
* Role-Based Authorization
* Admin-Only Routes (`require_admin`)
* Environment Variables using `python-dotenv`
* Secure Configuration with `.env`
* PostgreSQL Integration with SQLAlchemy
* Authentication and Authorization Best Practices

---

# Repository Structure

```text
Week_01_Python_Revision_OOP/
│
├── Day_01_Python_Fundamentals/
├── Day_02_Data_Structures/
├── Day_03_Functions/
├── Day_04_OOP/
├── Day_05_OOP_Part2/
└── Project_Library_Management_System/

Week_02_FastAPI/
│
├── Day_01_FastAPI_Basics/
├── Day_02_Pydantic_Models/
├── Day_03_SQLAIchemy_Database_Integration/
└── Day_04_Authentication/
```
