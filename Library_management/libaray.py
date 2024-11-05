from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrower = None
        self.due_date = None

    def lend_book(self, borrower_name):
        if self.is_available:
            self.is_available = False
            self.borrower = borrower_name
            self.due_date = datetime.now() + timedelta(days=14)  
            print(f"'{self.title}' has been lent to {borrower_name} and is due on {self.due_date.strftime('%Y-%m-%d')}.")
        else:
            print(f"'{self.title}' is already lent out to {self.borrower}.")

    def return_book(self):
        if not self.is_available:
            days_overdue = (datetime.now() - self.due_date).days
            fine = 0
            if days_overdue > 0:
                fine = days_overdue * 10  
                print(f"Book '{self.title}' is returned late. Fine: {fine} units.")
            else:
                print(f"Book '{self.title}' is returned on time.")
            
            
            self.is_available = True
            self.borrower = None
            self.due_date = None
        else:
            print(f"'{self.title}' was not lent out.")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def lend_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                book.lend_book(borrower_name)
                return
        print("Book not found in the library.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                return
        print("Book not found in the library.")

    def display_books(self):
        print(f"Books in {self.name} Library:")
        for book in self.books:
            status = "Available" if book.is_available else f"Lent out to {book.borrower} (Due: {book.due_date.strftime('%Y-%m-%d') if book.due_date else 'N/A'})"
            print(f"{book.title} by {book.author} - ISBN: {book.isbn} ({status})")


library = Library("City Library")

book1 = Book("The Catcher in the Rye", "J.D. Salinger", "1234")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "5678")


library.add_book(book1) 
library.add_book(book2)
library.display_books()


library.lend_book("1234", "John Doe")
library.display_books()

library.return_book("1234")
library.display_books()






"""
first create a book class
define the book name as title
whether it is available or not
author
borrower
due date



lend_book and define book u define in the book class
initilize all the varibale

another class as the library in the lib class
add the book
d
define af functiomj add book
lenf bool
disp;ay bool and the reeeturn book

create the obj of both the class
add the book and dispay it
then lenf the bool and collect the borrower name lsbn
check it is available or not
call the boo lend
()




"""