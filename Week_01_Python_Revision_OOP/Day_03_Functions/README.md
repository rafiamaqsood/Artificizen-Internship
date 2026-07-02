# Day 03 – Functions & Functional Tools

## Overview

This folder contains my practice exercises completed during **Day 03** of the internship training plan. The focus of this day was learning how to write reusable Python functions, use functional programming tools, understand variable scope, implement recursion, and organize code using modules.

---

## Topics Covered

### Functions

* Function Definition using `def`
* Parameters and Arguments
* Return Values
* Default Arguments
* Positional Arguments
* Keyword Arguments

### Variable-Length Arguments

* `*args`
* `**kwargs`

### Lambda Functions

* Anonymous Functions
* Using Lambda Expressions

### Functional Programming Tools

* `map()`
* `filter()`
* `zip()`
* `enumerate()`
* `sorted()` with `key`

### Scope

* Local Variables
* Global Variables
* `global` Keyword

### Recursion

* Recursive Functions
* Factorial
* Fibonacci

### Modules

* `import`
* `from ... import`
* Creating Custom Modules

---

## Practice Questions Implemented

### 1. Sum Any Number of Arguments Using `*args`

Write a function that accepts any number of arguments and returns their sum.

**Concepts Used**

* Functions
* `*args`
* Loops
* Return Statement

File:

```text
question_1_sum_args.py
```

---

### 2. Square Numbers Using `map()` and `lambda`

Use `map()` and a lambda function to square every number in a list.

**Concepts Used**

* `map()`
* Lambda Functions
* Lists

File:

```text
question_2_map_square.py
```

---

### 3. Filter Strings Longer Than Five Characters

Use `filter()` to extract all strings longer than five characters from a list.

**Concepts Used**

* `filter()`
* Lambda Functions
* String Length
* Lists

File:

```text
question_3_filter_strings.py
```

---

### 4. Recursive Factorial Function

Write a recursive function to calculate the factorial of a number.

**Concepts Used**

* Functions
* Recursion
* Base Case
* Recursive Calls

File:

```text
question_4_factorial.py
```

---

### 5. Sort Student Records by Marks

Sort a list of dictionaries containing student names and marks using `sorted()` and a key function.

**Concepts Used**

* Dictionaries
* `sorted()`
* Lambda Functions
* Key Functions

File:

```text
question_5_sort_students.py
```

---

### 6. Default Arguments and Mutable Default Values

Write a function with a default argument and explain why mutable default arguments should be avoided.

**Concepts Used**

* Default Arguments
* Functions
* Comments
* Mutable vs Immutable Objects

File:

```text
question_6_default_arguments.py
```

---

## Folder Structure

```text
Day_03_Functions_Functional_Tools/
│
├── question_1_sum_args.py
├── question_2_map_square.py
├── question_3_filter_strings.py
├── question_4_factorial.py
├── question_5_sort_students.py
├── question_6_default_arguments.py
└── README.md
```