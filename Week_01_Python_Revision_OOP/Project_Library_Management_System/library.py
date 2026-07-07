import json
from books import Book
from member import Member
from exceptions import *


class Library:
    FILE_NAME = "library.json"
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn, copies):

        if copies <= 0:
            raise ValueError("Copies must be greater than zero.")

        for book in self.books:
            if book.isbn == isbn:
                raise BookAlreadyExists("Book already exists.")

        new_book = Book(title, author, isbn, copies)
        self.books.append(new_book)

        print("Book added successfully!")

    def add_member(self, name, member_id):

        for member in self.members:
            if member.member_id == member_id:
                raise MemberAlreadyExists("Member already exists.")

        new_member = Member(name, member_id)
        self.members.append(new_member)

        print("Member added successfully!")
    
    def display_members(self):
        if not self.members:
            print("No members available.")
            return

        print("\n===== Members =====")

        for member in self.members:
            print(f"Name: {member.name}")
            print(f"Member ID: {member.member_id}")

            if member.borrowed_books:
                print("Borrowed Books:", ", ".join(member.borrowed_books))
            else:
                print("Borrowed Books: None")

    def search_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        raise BookNotFound("Book not found!")
    
    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.strip().lower() == title.strip().lower():
                return book
        raise BookNotFound("Book not found!")


    def issue_book(self, member_id, isbn):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is None:
            raise  MemberNotFound("Member not found!")
        book = self.search_book_by_isbn(isbn)
        if book.copies_available == 0:
            raise CopiesNotAvailable("No copies available!")
        if isbn in member.borrowed_books:
            raise AlreadyBorrowed("Member already has this book!")
        member.borrowed_books.append(isbn)
        book.copies_available -= 1
        print("Book issued successfully!")


    def return_book(self, member_id, isbn):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is None:
            raise MemberNotFound("Member not found!")
        if isbn not in member.borrowed_books:
            raise BookNotBorrowed("This book was never borrowed!")
        book = self.search_book_by_isbn(isbn)
        member.borrowed_books.remove(isbn)
        book.copies_available += 1
        print("Book returned successfully!")
    
    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n===== Books =====")

        for book in self.books:
            print(book)
            print("-" * 30)

    def save_data(self):
        data = {
            "books": [],
            "members": []
        }
        for book in self.books:
            data["books"].append({
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "copies": book.copies_available
            })
        for member in self.members:
            data["members"].append({
                "name": member.name,
                "member_id": member.member_id,
                "borrowed_books": member.borrowed_books
            })
        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully!")
    def load_data(self):
        try:

            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

            self.books = []
            self.members = []

            for b in data["books"]:
                book = Book(
                    b["title"],
                    b["author"],
                    b["isbn"],
                    b["copies"]
                )
                self.books.append(book)

            for m in data["members"]:
                member = Member(
                    m["name"],
                    m["member_id"]
                )

                member.borrowed_books = m["borrowed_books"]
                self.members.append(member)

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("No previous data found.")