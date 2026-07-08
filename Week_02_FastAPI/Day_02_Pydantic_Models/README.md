# Day 02 – Pydantic Models & Request/Response Validation

## Overview

This folder contains my solutions and practice exercises completed during **Day 02** of **Week 02** of the internship training plan. The focus of this day was learning how to use **Pydantic** with **FastAPI** to validate request data, define reusable schemas, create nested models, implement custom validation, and use response models to control API responses.

---

## Topics Covered

### Pydantic Models

* Creating models using `BaseModel`
* Type annotations
* Data validation
* Automatic type conversion

### Request Body Validation

* Accepting JSON request bodies
* Using Pydantic models as endpoint parameters
* Automatic request validation

### Field Constraints

* `Field()`
* `min_length`
* `max_length`
* `ge`
* `le`
* `gt`
* Regular expression (`pattern`) validation

### Optional Fields & Default Values

* `Optional`
* Default values
* `Field(default=...)`

### Nested Models

* Creating reusable schemas
* Embedding one model inside another
* Validating nested JSON objects

### Response Models

* Using `response_model`
* Filtering response data
* Returning validated API responses

### Custom Validation

* `@field_validator`
* Raising custom validation errors
* Validating individual fields

### Pydantic v2 Features

* `model_dump()`
* `ConfigDict(from_attributes=True)` for ORM compatibility

### Schema Separation

* `Create` schema for request data
* `Read` schema for response data

---

## Practice Questions Implemented

### 1. UserCreate Model & POST Endpoint

Created a `UserCreate` schema containing `name`, `email`, and `age`. Implemented a `POST /users` endpoint that accepts a JSON request body and returns the submitted user data.

**Concepts Used**

* `BaseModel`
* Request Body
* POST Endpoint
* JSON Response

File:

```text
question_1_user_create_model.py
```

---

### 2. Field Validation

Added validation constraints using `Field()`.

* Email must match a basic email pattern.
* Age must be between **18** and **120**.

**Concepts Used**

* `Field()`
* `pattern`
* `ge`
* `le`

File:

```text
question_2_field_validation.py
```

---

### 3. Response Model

Created a `UserRead` schema that extends `UserCreate` by adding an `id` field. Used `response_model` to ensure the API response always contains an ID.

**Concepts Used**

* Schema Inheritance
* `response_model`
* Response Validation

File:

```text
question_3_response_model.py
```

---

### 4. Nested Models

Created an `Address` schema with `city` and `country`, then embedded it inside the `UserCreate` model.

**Concepts Used**

* Nested Models
* Model Composition
* Nested JSON Validation

File:

```text
question_4_nested_models.py
```

---

### 5. Custom Field Validation

Implemented a `@field_validator` to reject any user name containing numeric characters.

**Concepts Used**

* `@field_validator`
* Custom Validation
* Raising `ValueError`

File:

```text
question_5_field_validator.py
```

---

### 6. Product Create & Read Schemas

Created separate `ItemCreate` and `ItemRead` schemas for product data. The read schema includes a `created_at` timestamp, and `response_model` ensures it is always included in API responses.

**Concepts Used**

* Create vs Read Schemas
* `response_model`
* `model_dump()`
* `datetime`

File:

```text
question_6_item_schemas.py
```

---

### 7. Advanced Pydantic Model Practice

Created a comprehensive `Patient` model to practice advanced Pydantic features, including specialized data types, metadata using `Annotated`, strict field validation, optional fields, collection types, dictionaries, and custom email domain validation.

**Concepts Used**

* `Annotated`
* `Field()` metadata (`title`, `description`, `examples`)
* `EmailStr`
* Strict type validation
* Optional fields
* `List`
* `Dict`
* Custom `@field_validator`
* Domain-specific email validation
* Type conversion
* Pydantic model instantiation

File:

```text
practice.py
```

---

## Folder Structure

```text
Day_02_Pydantic_Models/
│
├── question_1_user_create_model.py
├── question_2_field_validation.py
├── question_3_response_model.py
├── question_4_nested_models.py
├── question_5_field_validator.py
├── question_6_item_schemas.py
├── practice.py
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
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

