# Day 04 – Object-Oriented Programming (OOP) Part 1

## Overview

This folder contains my practice exercises completed during **Day 04** of the internship training plan. The focus of this day was learning the fundamentals of **Object-Oriented Programming (OOP)** in Python, including creating classes and objects, using constructors, understanding instance and class variables, implementing different types of methods, applying encapsulation, and using properties for controlled attribute access.

---

## Topics Covered

### Classes and Objects

* Defining Classes
* Creating Objects (Instances)
* Object-Oriented Programming Basics

### Constructors

* `__init__()` Constructor
* `self` Keyword
* Initializing Object Attributes

### Variables

* Instance Variables
* Class Variables

### Methods

* Instance Methods
* `@classmethod`
* `@staticmethod`

### Encapsulation

* Public Attributes
* Protected Attributes (`_attribute`)
* Private Attributes (`__attribute`)

### Properties

* `@property`
* Read-Only Properties
* Controlled Attribute Access (Getters)

---

## Practice Questions Implemented

### 1. Create a Car Class

Create a `Car` class with attributes (`brand`, `model`, `year`) and a method to display the car's information.

**Concepts Used**

* Classes
* Objects
* `__init__()`
* Instance Variables
* Instance Methods

File:

```text
question_1_car_class.py
```

---

### 2. Create a BankAccount Class

Create a `BankAccount` class with `deposit()` and `withdraw()` methods. Prevent withdrawals that exceed the available balance and validate deposit/withdrawal amounts.

**Concepts Used**

* Classes
* Constructors
* Instance Variables
* Conditional Statements
* Instance Methods

File:

```text
question_2_bank_account.py
```

---

### 3. Demonstrate Instance vs Class Variables

Create a `Student` class to demonstrate the difference between instance variables and class variables by tracking how many objects have been created.

**Concepts Used**

* Class Variables
* Instance Variables
* Constructors
* Object Counter

File:

```text
question_3_instance_vs_class_variables.py
```

---

### 4. Private Attribute with `@property`

Create a class with a private attribute and expose it safely using the `@property` decorator.

**Concepts Used**

* Encapsulation
* Private Attributes
* `@property`
* Getters

File:

```text
question_4_property.py
```

---

### 5. Alternate Constructor Using `@classmethod`

Create a `Person` class with an alternate constructor `from_birth_year()` that calculates a person's age from their birth year.

**Concepts Used**

* `@classmethod`
* Alternate Constructors
* Constructors
* Class Methods

File:

```text
question_5_classmethod.py
```

---

## Folder Structure

```text
Day_04_Object_Oriented_Programming_Part_1/
│
├── question_1_car_class.py
├── question_2_bank_account.py
├── question_3_instance_vs_class_variables.py
├── question_4_property.py
├── question_5_classmethod.py
└── README.md
```