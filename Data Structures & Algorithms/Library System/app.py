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
    def saveData(self):
        data = {
            'books': self.books,
            'patrons': self.patrons
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
    def addPatron(self, patron):
        if any(existingPatron.name == patron.name for existingPatron in self.patrons):
            print(f"Sorry, someone with the name {patron.name} already exists in the library system.")
        else:
            self.patrons.append(patron)
            print(f"Thank you for registering {patron.name}. Their ID Number is {patron.IDNumber}.")
        self.saveData
    def displayAllPatrons(self):
        print("All Patrons:")
        for patron in self.patrons:
            print(f"Patron Name: {patron.name}, Patron Date of Birth: {patron.birthday}, Patron ID: {patron.IDNumber}")
    def displayPatronFines(self):
        print("All Patrons with Fines")
        for patron in self.patrons:
            print(f"Patron Name: {patron.name}, Fine: {patron.fine}")
    def IDExists(self, IDNumber):
        for patron in self.patrons:
            if patron.IDNumber == IDNumber:
                return True
        else: return False
class Book:
    def __init__(self, title, publishedYear, author):
        self.title = title
        self.publishedYear = publishedYear
        self.author = author
        self.dueDate = None
        self.rentingPatron = None
        print(f"{self.title} by {self.author}, published in {self.publishedYear}, arrived.")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publishedYear}"
    def checkOut(self, patron):
        if patron.fine > 0:
            print(f"Sorry {patron.name}, you can't check out {self.title} because you have a fine of ${patron.fine:.2f}")
        elif patron not in library.patrons:
            print(f"Sorry {patron.name}, you can't check out {self.title} because you're not in the libary system.")
        elif self.dueDate == None:
            today = datetime.date.today()
            self.rentingPatronName = patron.name
            self.rentingPatronID = patron.IDNumber
            self.dueDate = today + datetime.timedelta(days = 14)
            print(f"Thanks, {self.rentingPatronName} (ID Number: {self.rentingPatronID}), for checking out {self.title}. This book is due on {self.dueDate}.")
            library.saveData()
        else:
            print(f"Sorry, {patron.name}, {self.title} is checked out. It should be returned on or before {self.dueDate}.")
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
    def __init__(self, name, birthMonth, birthDay, birthYear):
        self.name = name
        self.birthday = datetime.date(birthYear, birthMonth, birthDay)
        self.IDNumber = self.generateIDNumber()
        self.fine = 0
        library.addPatron(self)
    def generateIDNumber(self):
        while True:
            IDNumber = (''.join(random.choices(string.digits, k=6)))
            if not library.IDExists(IDNumber):
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

hero = Book("Hero on a Mission: A Path to a Meaningful Life", "2023", "Donald Miller")
print("\n")

library.addBook(hero)
print("\n")

library.displayAllBooks()
print("\n")

chase = Patron("Chase Tramel", 3, 15, 1995)
print("\n")

library.displayBooksByStatus()
print("\n")

library.displayAllPatrons()
print("\n")

if __name__ == '__main__':
    app.run()