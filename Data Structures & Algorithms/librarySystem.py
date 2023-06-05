# A Python program to simulate a library system
# K Chase Tramel - https://github.com/ChaseTramel

import datetime
import random
import string

class Library:
    def __init__(self):
        self.books = [] # List of book objects
        self.fines = {} # Dictionary to associate fines with patrons
    def addBook(self, book):
        self.books.append(book)
        print(f"{book.title} was just added to the library.")
    def removeBook(self, book):
        self.books.remove(book)
    def searchBookByTitle(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return
    def searchBookByAuthor(self, author):
        for book in self.books:
            if book.author == author:
                return book
        return
    def displayAllBooks(self):
        print("All Libary Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}")
    def displayBooksByStatus(self):
        print("Books Checked Out:")
        for book in self.books:
            if book.dueDate is not None:
                print(f"Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}, Due: {book.dueDate}")
        print("Books Not Checked Out:")
        for book in self.books:
            if book.dueDate is None:
                print(f"Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}")
class Book:
    def __init__(self, title, publishedYear, author):
        self.title = title
        self.publishedYear = publishedYear
        self.author = author
        self.dueDate = None
        self.rentingPatron = None
        self.fine = 0 # Initilized with no fine
        print(f"{self.title} by {self.author}, published in {self.publishedYear}, arrived.")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publishedYear}"
    def checkOut(self, patronName, patronID):
        if patronID in library.fines and library.fines[patronID] > 0:
            print(f"Sorry {patronName}, you can't check out this book because you have a fine of ${library.fines[patronID]:.2f}")
        elif self.dueDate == None:
            today = datetime.date.today()
            self.rentingPatronName = patronName
            self.rentingPatronID = patronID
            self.dueDate = today + datetime.timedelta(days = 14)
            print(f"Thanks, {self.rentingPatronName} (ID Number: {self.rentingPatronID}), for checking out {self.title}. This book is due on {self.dueDate}.")
        else:
            print(f"Sorry, {patronName}, that book is checked out. It should be returned on or before {self.dueDate}.")
    def returnBook(self):
        if self.dueDate is not None:
            self.calculateFine()
            self.rentingPatron = None
            self.rentingPatronID = None
            self.dueDate = None
            if self.fine > 0:
                if self.rentingPatronID in library.fines:
                    library.fines[self.rentingPatronID] += self.fine
                else:
                    library.fines[self.rentingPatronID] = self.fine
                print(f"You've now returned {self.title}, but it was late, so you have a fine of ${library.fines[self.rentingPatronID]:.2f}.")
            else:
                print(f"You've now returned {self.title}!")
        else:
            print(f"{self.title} can't be returned because it isn't checked out!")
    def calculateFine(self):
        if self.dueDate is not None and self.dueDate < datetime.date.today():
            daysLate =(datetime.date.today() - self.dueDate).days
            self.fine = daysLate * .25 # Late fee of  25 cents per day
        else:
            self.fine = 0
    def displayStatus(self):
        if self.dueDate is None:
            print(f"{self.title} by {self.author}, published in {self.publishedYear}, is not currently checked out.")
        else:
            print(f"{self.title} by {self.author}, published in {self.publishedYear}, is currently checked out and due {self.dueDate}.")

class Patron:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.IDNumber = (''.join(random.choices(string.digits, k=6)))
    def __str__(self):
        return f"Thank you for registering {self.name}, DOB: {self.birthday}. Their ID Number is {self.IDNumber}."

class Librarian:
    pass

# Initialize Library
library = Library()

# Add books to world and system
gatsby = Book("The Great Gatsby", "1925", "F. Scott Fitzgerald")
library.addBook(gatsby)
mockingbird = Book("To Kill a Mockingbird", "1960", "Harper Lee")
library.addBook(mockingbird)
hunterAbe = Book("Abraham Lincoln, Vampire Hunter", "2010", "Seth Grahame-Smith")
library.addBook(hunterAbe)
print("\n")

# Add patrons to system
chaseTramel = Patron("Chase Tramel", datetime.date(1995, 4, 17))
print(chaseTramel)
warrenJones = Patron("Warren Jones", datetime.date(1966, 12, 28))
print(warrenJones)
print("\n")

# Chase checks out The Great Gatsby
gatsby.checkOut(chaseTramel.name, chaseTramel.IDNumber)
print("\n")

# Warren tries to check out The Great Gatsby, but it's already checked out
gatsby.checkOut(warrenJones.name, warrenJones.IDNumber)
print("\n")

# Check the status of To Kill a Mockingbird
mockingbird.displayStatus()
print("\n")

# Warren checks out To Kill a Mockingbird instead
mockingbird.checkOut(warrenJones.name, warrenJones.IDNumber)
print("\n")

# Check the status of To Kill a Mockingbird
mockingbird.displayStatus()
print("\n")

# Display all of the books in the system
library.displayAllBooks()
print("\n")

# Display the books that are checked out and that aren't checked out
library.displayBooksByStatus()
print("\n")

# Chase returns The Great Gatsby
gatsby.returnBook()
print("\n")

# Warren tries to return Abraham Lincoln, Vampire Hunter, even though it isn't checked out.
hunterAbe.returnBook()
print("\n")

# Manually giving Chase fines for testing
library.fines[chaseTramel.IDNumber] = 3
hunterAbe.checkOut(chaseTramel.name, chaseTramel.IDNumber)
print("\n")