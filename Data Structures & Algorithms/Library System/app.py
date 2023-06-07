# A Python program to simulate a library system
# K Chase Tramel - https://github.com/ChaseTramel

import datetime
import random
import string
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

class Library:
    def __init__(self):
        self.books = [] # List of book objects
        self.patrons = [] # List of patron objects
    def saveData(self):
        data = {
            'books':[book.__dict__ for book in self.books],
            'patrons':[patron.__dict__ for patron in self.patrons]
        }
        filepath = "Data Structures & Algorithms\Library System\libraryData.json"
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4, default=str)
        print("Library data backed up successfully!")
    def loadData(self):
        filepath = "Data Structures & Algorithms\Library System\libraryData.json"
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            self.books = [Book(**book) for book in data['books']]
            self.patrons = [Patron(**patron) for patron in data['patrons']]
            for book in self.books:
                if book.rentingPatron:
                    patron_id = book.rentingPatron
                    for patron in self.patrons:
                        if patron.IDNumber == patron_id:
                            book.rentingPatron = patron.name
                            break
            print("Library data loaded successfully!")
        except FileNotFoundError:
            print("Library data not found. A new library file was made.")
        except json.JSONDecodeError:
            print("Error loading the library data. The file may be corrupted.")
    def addBook(self, title, pubYear, author, dueDate, rentingPatron, bookID):
        book = Book(title, pubYear, author, dueDate, rentingPatron, bookID)
        if any(existingBook.title == book.title for existingBook in self.books):
            print(f"Sorry, a book with the title '{book.title}' is already in the library.")
        else: 
            self.books.append(book)
            print(f"{book.title} was just added to the library.")
            self.saveData()
    def removeBook(self, book):
        self.books.remove(book)
        self.saveData()
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
            print(f"BookID: {book.bookID}, Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}")
    def displayBooksByStatus(self):
        print("Books Checked Out:")
        for book in self.books:
            if book.dueDate is not None:
                print(f"BookID: {book.bookID}, Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}, Due: {book.dueDate}")
        print("Books Not Checked Out:")
        for book in self.books:
            if book.dueDate is None:
                print(f"BookID: {book.bookID}, Title: {book.title}, Author: {book.author}, Published Year: {book.publishedYear}")
    def addPatron(self, patron):
        if any(existingPatron.name == patron.name for existingPatron in self.patrons):
            print(f"Sorry, someone with the name {patron.name} already exists in the library system.")
        else:
            self.patrons.append(patron)
            print(f"Thank you for registering {patron.name}. Their ID Number is {patron.IDNumber}.")
            self.saveData()
    def displayAllPatrons(self):
        print("All Patrons:")
        for patron in self.patrons:
            print(f"Patron Name: {patron.name}, Patron Date of Birth: {patron.birthday}, Patron ID: {patron.IDNumber}")
    def displayPatronFines(self):
        print("All Patrons with Fines")
        for patron in self.patrons:
            print(f"Patron Name: {patron.name}, Fine: {patron.fine}")
    def patronIDExists(self, IDNumber):
        for patron in self.patrons:
            if patron.IDNumber == IDNumber:
                return True
        else: return False
    def bookIDExists(self, bookID):
        for book in self.books:
            if book.bookID == bookID:
                return True
        else: return False
    def findPatron(self, IDNumber):
        for patron in self.patrons:
            if patron.IDNumber == IDNumber:
                print(f"{patron.name} found!")
                return patron
        print("Patron not found.")
        return None
    def findBook(self, bookID):
        for book in self.books:
            if book.bookID == bookID:
                print(f"{book.title} found!")
                return book
        print("Book not found")
        return None
class Book:
    def __init__(self, title, publishedYear, author, dueDate, rentingPatron, bookID):
        self.title = title
        self.publishedYear = publishedYear
        self.author = author
        self.dueDate = dueDate
        self.rentingPatron = rentingPatron
        self.bookID = bookID
        if bookID == None:
            self.bookID = self.generateBookID()
        print(f"{self.title} by {self.author}, published in {self.publishedYear}, arrived.")
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)
    def __repr__(self):
        return self.__str__()
    def serialize(self):
        return self.__str__
    def generateBookID(self):
        while True:
            attemptedID = (''.join(random.choices(string.digits, k=8)))
            if not library.bookIDExists(attemptedID):
                return attemptedID
    def checkOut(self, IDNumber):
        patron = library.findPatron(IDNumber)
        if patron.fine > 0:
            print(f"Sorry {patron.name}, you can't check out {self.title} because you have a fine of ${patron.fine:.2f}")
        elif patron not in library.patrons:
            print(f"Sorry {patron.name}, you can't check out {self.title} because you're not in the libary system.")
        elif self.dueDate == None:
            today = datetime.date.today()
            self.rentingPatron = patron.name
            self.dueDate = today + datetime.timedelta(days = 14)
            print(f"Thanks, {patron.name} (ID Number: {patron.IDNumber}), for checking out {self.title}. This book is due on {self.dueDate}.")
            library.saveData()
        else:
            print(f"Sorry, {patron.name}, {self.title} is checked out. It should be returned on or before {self.dueDate}.")
    def returnBook(self):
        if self.dueDate is not None:
            self.calculateFine()
            self.rentingPatron = None
            self.dueDate = None
        else:
            print(f"{self.title} can't be returned because it isn't checked out!")
        library.saveData()
    def calculateFine(self):
        if self.dueDate is not None and self.dueDate < datetime.date.today():
            daysLate =(datetime.date.today() - self.dueDate).days
            self.fine = daysLate * .25 # Late fee of  25 cents per day
        else:
            self.fine = 0
        library.saveData()
    def displayStatus(self):
        if self.dueDate is None:
            print(f"{self.title} by {self.author}, published in {self.publishedYear}, is not currently checked out.")
        else:
            print(f"{self.title} by {self.author}, published in {self.publishedYear}, is currently checked out and due {self.dueDate}.")

class Patron:
    def __init__(self, name, birthday, IDNumber, fine = 0):
        self.name = name
        self.birthday = birthday
        self.fine = fine
        self.IDNumber = IDNumber
        if self.IDNumber == None:
            self.IDNumber = self.generateIDNumber()
        library.addPatron(self)
    def generateIDNumber(self):
        while True:
            IDNumber = (''.join(random.choices(string.digits, k=6)))
            if not library.patronIDExists(IDNumber):
                return IDNumber
    def payFine(self, payment):
        print(f"{self.name}, you have a fine of ${self.fine:.2f}")
        if self.fine > 0:
            self.fine -= payment
            print(f"You paid ${payment:.2f} towards you fine balance. Your balance is now ${self.fine:.2f}.")
            if self.fine < 0:
                change = abs(self.fine)
                print(f"Here's your change of ${change:.2f}")
                self.fine = 0
                print(f"Your balance is now ${self.fine:.2f}.")
            library.saveData()



# Initialize Library
library = Library()
library.loadData()
print("\n")

library.addBook("Frankenstein", "1818", "Mary Shelley", None, None, None)
print("\n")

Patron("Chase Tramel", "3-13-1994", None)
print("\n")

library.displayBooksByStatus()
print("\n")

library.findBook("55772265").checkOut("582053")


if __name__ == '__main__':
    app.run()