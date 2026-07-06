# Day 05 – Object-Oriented Programming (OOP) Part 2 + Practical Python

## Overview

This folder contains my practice exercises completed during **Day 05** of the internship training plan. The focus of this day was learning advanced **Object-Oriented Programming (OOP)** concepts in Python, including inheritance, polymorphism, abstraction, magic (dunder) methods, exception handling, file handling, JSON operations, and other practical Python topics commonly used in real-world applications.

---

## Topics Covered

### Inheritance

* Single Inheritance
* Multiple Inheritance
* `super()`

### Polymorphism

* Method Overriding
* Duck Typing

### Abstraction

* Abstract Base Classes (ABC)
* `@abstractmethod`

### Dunder (Magic) Methods

* `__str__()`
* `__repr__()`
* `__len__()`
* `__eq__()`
* `__add__()`

### Exception Handling

* `try`
* `except`
* `else`
* `finally`
* Raising Custom Exceptions

### File Handling

* Reading Files
* Writing Files
* Context Managers (`with` Statement)

### Working with JSON

* `json.dump()`
* `json.dumps()`
* `json.load()`
* `json.loads()`

### Practical Python

* Virtual Environments (`venv`)
* `pip`
* `requirements.txt`
* Basic Type Hints

---

## Practice Questions Implemented

### 1. Inheritance and Method Overriding

Create a base `Animal` class with a `speak()` method and implement `Dog` and `Cat` subclasses that override the method.

**Concepts Used**

* Inheritance
* Method Overriding
* Polymorphism

File:

```text
question_1_inheritance.py
```

---

### 2. Custom Exception in BankAccount

Create a custom `InsufficientBalanceError` exception and raise it when attempting to withdraw more money than the available account balance.

**Concepts Used**

* Custom Exceptions
* `raise`
* Exception Handling
* Classes and Objects

File:

```text
question_2_custom_exception.py
```

---

### 3. File Statistics

Read a text file and report the total number of lines, words, and characters.

**Concepts Used**

* File Handling
* Context Managers (`with`)
* String Methods

File:

```text
question_3_file_statistics.py
```

---

### 4. Working with JSON

Save a list of student records (dictionaries) into a JSON file and then load the data back into Python.

**Concepts Used**

* JSON Serialization
* `json.dump()`
* `json.load()`
* File Handling

File:

```text
question_4_json.py
```

---

### 5. Implement `__str__()` and `__repr__()`

Create a `Point` class and implement the `__str__()` and `__repr__()` magic methods to provide meaningful object representations.

**Concepts Used**

* Dunder (Magic) Methods
* Object Representation
* OOP

File:

```text
question_5_dunder_methods.py
```

---

### 6. Exception Handling

Write a program that gracefully handles multiple exception types using `try`, `except`, `else`, and `finally`.

**Concepts Used**

* `try`
* `except`
* `else`
* `finally`
* `ValueError`
* `ZeroDivisionError`
* `FileNotFoundError`

File:

```text
question_6_exception_handling.py
```

---

## Folder Structure

```text
Day_05_OOP_Part_2_Practical_Python/
│
├── question_1_inheritance.py
├── question_2_custom_exception.py
├── question_3_file_statistics.py
├── question_4_json.py
├── question_5_dunder_methods.py
├── question_6_exception_handling.py
└── README.md
```