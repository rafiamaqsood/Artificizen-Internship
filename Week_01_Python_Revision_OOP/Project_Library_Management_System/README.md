# Library Management System (CLI)

A simple **Command Line Interface (CLI) Library Management System** built in **Python** as the **Week 1 Capstone Project** for the Artificizen AI Engineer Internship.

The project demonstrates core Python concepts including Object-Oriented Programming (OOP), file handling, JSON persistence, exception handling, and input validation.

---

## Features

- Add new books
- Register new members
- Search books
  - By ISBN
  - By Title
- Issue books to members
- Return issued books
- View all books
- View all members
- Save library data to JSON
- Load previously saved data automatically
- Custom exception handling
- Input validation for user-friendly CLI

---

## Project Structure

```
Project_Library_Management_System/
│
├── main.py              # CLI and menu system
├── library.py           # Library management logic
├── books.py             # Book class
├── member.py            # Member class
├── exceptions.py        # Custom exceptions
├── library.json         # Stores library data
└── README.md
```

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling

---

## OOP Concepts Implemented

### Classes & Objects

- Book
- Member
- Library

### Constructors

- `__init__()`

### Magic Method

- `__str__()`

### Object Composition

The `Library` class manages collections of `Book` and `Member` objects.

---

## Custom Exceptions

The project uses custom exceptions for better error handling.

- `BookNotFound`
- `BookAlreadyExists`
- `MemberNotFound`
- `MemberAlreadyExists`
- `CopiesNotAvailable`
- `AlreadyBorrowed`
- `BookNotBorrowed`

---

## JSON Persistence

All library data is stored inside:

```
library.json
```

The program:

- Loads data automatically when it starts.
- Saves data automatically when exiting.

This allows data to persist between program executions.

---

## Menu

```
===== Library Management System =====

1. Add Book
2. Add Member
3. Search Book
4. Issue Book
5. Return Book
6. View All Books
7. View All Members
8. Exit
```

---

## Search Options

Books can be searched using:

- ISBN
- Title

---

## Input Validation

The application validates user input to prevent invalid data.

Examples include:

- Empty book titles
- Empty member IDs
- Invalid ISBNs
- Non-numeric ISBNs
- Invalid menu choices
- Invalid number of copies
- Negative copy counts

---

## Sample Output

```
===== Library Management System =====

1. Add Book
2. Add Member
3. Search Book
4. Issue Book
5. Return Book
6. View All Books
7. View All Members
8. Exit

Enter your choice: 1

Enter book title: Harry Potter
Enter author name: J.K. Rowling
Enter ISBN: 1234
Enter number of copies: 5

Book added successfully!
```

