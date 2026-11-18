# PART 1 - GREETER CLASS
class Greeter:
    def __init__(self, name):
        self.name = name

        def greet(self):
            print(f"Hello, {self.name}! Welcome to OOP in Python.")

            g = Greeter("student")
            g.greet()

# PART 2 & 3: Car Class, Methods & Objects
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Ford", "Mustang", 2023)
car2 = Car("BMW", "X5", 2022)
car3 = Car("Tesla", "Model 3", 2024)
 
print("CAR 1")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Year:", car1.year)
print("Wheels:", car1.wheels)

print("\nCAR 2")
print("Brand:", car2.brand)
print("Model:", car2.model)
print("Year:", car2.year)
print("Wheels:", car2.wheels)

print("\nCAR 3")
print("Brand:", car3.brand)
print("Model:", car3.model)
print("Year:", car3.year)
print("Wheels:", car3.wheels)

# PART 4 - LIBRARY BOOK CLASS

class Book:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

        Book.counter += 1
        self.book_id = Book.counter

    def borrow(self):
        if self.borrowed:
            print("This book is already borrowed.")
        else:
            self.borrowed = True
            print(self.title, "has been borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(self.title, "has been returned.")
        else:
            print("This book was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book1 = Book("The Fault in Our Stars", "John Green")
book2 = Book("Wonder", "R.J. Palacio")
book3 = Book("Percy Jackson", "Rick Riordan")

print("\nLIBRARY BOOK LIST")
print(book1)
print(book2)
print(book3)

print("\nBORROWING BOOKS")
book1.borrow()
book2.borrow()

book1.borrow()

print("\nRETURNING BOOK")
book1.return_book()

print("\nUPDATED BOOK LIST")
print(book1)
print(book2)
print(book3)

print("\nTotal books:", Book.counter)

print("\nBook representation:")
print(repr(book1))

