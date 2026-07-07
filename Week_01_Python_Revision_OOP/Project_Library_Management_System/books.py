class Book:

    def __init__(self, title, author, isbn, copies_available):
            self.title =title
            self.author = author
            self.isbn =isbn
            self.copies_available = copies_available 
    def __str__(self):
          return (
                f"Title : {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN  : {self.isbn}\n"
                f"Copies: {self.copies_available}"
                )