# A Python program to simulate a library system
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

import datetime
import random
import string

class Book:
    def __init__(self, title, publishedYear, author):
        self.title = title
        self.publishedYear = publishedYear
        self.author = author
        self.dueDate = None
        self.rentingPatron = None
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publishedYear}, was added to the system."
    def checkOut(self, patronName, patronID):
        today = datetime.date.today()
        self.rentingPatronName = patronName
        self.rentingPatronID = patronID
        self.dueDate = today + datetime.timedelta(days = 14)
        print(f"Thanks, {self.rentingPatronName} (ID Number: {self.rentingPatronID}), for checking out {self.title}. This book is due on {self.dueDate}.")

class Patron:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.IDNumber = (''.join(random.choices(string.digits, k=10)))
    def __str__(self):
        return f"Thank you for registering {self.name}, DOB: {self.birthday}. Their ID Number is {self.IDNumber}."

class Librarian:
    pass

gatsby = Book("The Great Gatsby", "1925", "F. Scott Fitzgerald")

print(gatsby)
newPatron = Patron("Chase", datetime.date.today())
print(newPatron)
gatsby.checkOut(newPatron.name, newPatron.IDNumber)