# A Python program to simulate a library system
# K Chase Tramel - https://github.com/ChaseTramel

import datetime
import random
import string
import pickle
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
        self.fines = {} # Dictionary to associate fines with patrons
    def saveData(self):
        data = {
            'books': self.books,
            'patrons': self.patrons,
            'fines': self.fines
        }
        with open("libraryFile.txt", 'wb') as file:
            pickle.dump(data,file)
        print("Library backed up successfully.")
    def loadData(self):
        try:
            with open("libraryFile.txt", 'rb') as file:
                data = pickle.load(file)
            self.books = data['books']
            self.patrons = data['patrons']
            self.fines = data['fines']
            print("Library data loaded successfully.")
        except FileNotFoundError:
            print("Library file not found!")
        except pickle.UnpicklingError:
            print("Error loading library data. The file may be corrupted.")     
    def addBook(self, book):
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
    def displayAllPatrons(self):
        print("All Patrons:")
        for patron in self.patrons:
            print(f"Patron Name: {patron.name}, Patron Date of Birth: {patron.birthday}, Patron ID: {patron.IDNumber}")
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
            print(f"Sorry {patronName}, you can't check out {self.title} because you have a fine of ${library.fines[patronID]:.2f}")
        elif self.dueDate == None:
            today = datetime.date.today()
            self.rentingPatronName = patronName
            self.rentingPatronID = patronID
            self.dueDate = today + datetime.timedelta(days = 14)
            print(f"Thanks, {self.rentingPatronName} (ID Number: {self.rentingPatronID}), for checking out {self.title}. This book is due on {self.dueDate}.")
        else:
            print(f"Sorry, {patronName}, {self.title} is checked out. It should be returned on or before {self.dueDate}.")
        library.saveData()
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
                print(f"{self.title} was returned, but it was late, so you have a fine of ${library.fines[self.rentingPatronID]:.2f}.")
            else:
                print(f"{self.title}, was returned!")
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
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.IDNumber = (''.join(random.choices(string.digits, k=6)))
        self.fine = 0
        library.patrons.append(self)
    def __str__(self):
        return f"Thank you for registering {self.name}, DOB: {self.birthday}. Their ID Number is {self.IDNumber}."
    def payFine(self, payment):
        if self.IDNumber in library.fines:  # If the patron is in the fine dictionary
            if library.fines[self.IDNumber] > 0:
                print(f"Thanks {self.name}, you paid your fine of ${library.fines[self.IDNumber]:.2f}.")
                library.fines[self.IDNumber] -= payment
                print(f"Your balance is now ${library.fines[self.IDNumber]:.2f}.")
                if library.fines[self.IDNumber] < 0:  # if Patron gave too much money
                    change = abs(library.fines[self.IDNumber])
                    print(f"Here is your change of ${change:.2f}")
                    library.fines[self.IDNumber] = 0
                    print(f"Your balance is now ${library.fines[self.IDNumber]:.2f}.")
            else:
                print(f"Thanks {self.name}, you contributed towards your fine of ${library.fines[self.IDNumber]:.2f}.")
                library.fines[self.IDNumber] -= payment
                print(f"Your balance is now ${library.fines[self.IDNumber]:.2f}.")
        else:
            print(f"{self.name}, you didn't have any fines to pay!")
        library.saveData()



# Initialize Library
library = Library()
library.loadData()

# Display all of the books in the system
library.displayAllBooks()
print("\n")

# Display the books that by status
library.displayBooksByStatus()
print("\n")

# Display all patrons
library.displayAllPatrons()
print("\n")

# Display all patron balances
library.displayPatronBalances()
print("\n")

# Add a book to the system
hero = Book("Hero on a Mission: A Path to a Meaningful Life", "2023", "Donald Miller")
print("\n")
library.addBook(hero)
print("\n")

# Display all of the books in the system
library.displayAllBooks()
print("\n")

if __name__ == '__main__':
    app.run()