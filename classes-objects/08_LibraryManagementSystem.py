# Problem 8: Library Management System
# Scenario: Manage library books
# Task: Borrow and return books

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):

        if self.available:
            self.available = False
            print("Book borrowed successfully.")

        else:
            print("Book is not available.")

    def return_book(self):

        self.available = True
        print("Book returned successfully.")


# Creating object
book = Book("Python Essentials", "Mark")

# Calling methods
book.borrow()
book.return_book()