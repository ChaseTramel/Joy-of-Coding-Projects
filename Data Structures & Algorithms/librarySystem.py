# A Python program to simulate a library system
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import datetime

class Book:
    def __init__(self, name, year, author, dueDate):
        self.name = name
        self.year = year
        self.author = author
        self.dueDate = None
        self.renter = None
    def __str__(self):
        return f"{self.name} by {self.author} is due on {self.dueDate}"
    def checkOut(self, renter):
        today = datetime.date.today()
        self.renter = renter
        self.dueDate = today + datetime.timedelta(days = 14)
        print(f"Thanks {self.renter} for checking out {self.name}. This book is due on {self.dueDate}")

gatsby = Book("The Great Gatsby", "1925", "Gatsby Author", datetime.date(2023, 5, 28))

print(gatsby)
gatsby.checkOut("Chase")