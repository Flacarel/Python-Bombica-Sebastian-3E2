#1
import math
class Shape:
    def area(self):
        print("Area calculation is not implemented for this shape.")
        return None

    def perimeter(self):
        print("Perimeter calculation is not implemented for this shape.")
        return None


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

shape = Shape()
print("Shape area:", shape.area())
print("Shape perimeter:", shape.perimeter())

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())
#######
#2
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest amount: ${interest}")
        return interest

    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Overdraft limit exceeded.")
        else:
            print("Withdrawal amount must be positive.")
savings = SavingsAccount("S123", 1000, interest_rate=0.05)
savings.deposit(200)
savings.apply_interest()
print("Savings balance:", savings.get_balance())

checking = CheckingAccount("C456", 500, overdraft_limit=200)
checking.withdraw(600)
print("Checking balance:", checking.get_balance())
checking.withdraw(200)
#######
#3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, gallons):
        mileage = self.fuel_efficiency * gallons
        print(f"Car can travel {mileage} miles with {gallons} gallons.")
        return mileage

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, gallons):
        mileage = self.fuel_efficiency * gallons
        print(f"Motorcycle can travel {mileage} miles with {gallons} gallons.")
        return mileage

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self, load_weight):
        if load_weight <= self.towing_capacity:
            print(f"Truck can tow the load of {load_weight} pounds.")
            return True
        else:
            print(f"Truck cannot tow the load of {load_weight} pounds; exceeds towing capacity.")
            return False

car = Car("Toyota", "Camry", 2022, fuel_efficiency=30)
car.display_info()
car.calculate_mileage(10)

motorcycle = Motorcycle("Harley-Davidson", "Iron 883", 2021, fuel_efficiency=45)
motorcycle.display_info()
motorcycle.calculate_mileage(5)

truck = Truck("Ford", "F-150", 2023, towing_capacity=13000)
truck.display_info()
truck.calculate_towing_capacity(12000)
truck.calculate_towing_capacity(14000)  # Exceeds capacity
##########
#4
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Info: Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}")

    def get_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} people.")

    def get_annual_salary(self):
        # Managers receive a bonus based on team size
        bonus = 500 * self.team_size
        return super().get_annual_salary() + bonus

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, specialty):
        super().__init__(name, employee_id, salary)
        self.specialty = specialty

    def work_on_project(self, project_name):
        print(f"{self.name}, who specializes in {self.specialty}, is working on {project_name}.")

    def get_annual_salary(self):
        # Engineers receive a flat annual bonus
        bonus = 3000
        return super().get_annual_salary() + bonus

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission_rate):
        super().__init__(name, employee_id, salary)
        self.commission_rate = commission_rate

    def calculate_commission(self, sales_amount):
        commission = self.commission_rate * sales_amount
        print(f"{self.name} earned a commission of ${commission} on sales of ${sales_amount}.")
        return commission

    def get_annual_salary(self, annual_sales=0):
        # Salespersons receive commission based on annual sales
        commission = self.calculate_commission(annual_sales)
        return super().get_annual_salary() + commission

manager = Manager("Alice", 101, 5000, team_size=10)
manager.display_info()
manager.manage_team()
print("Manager Annual Salary:", manager.get_annual_salary())

engineer = Engineer("Bob", 102, 4000, specialty="Software Development")
engineer.display_info()
engineer.work_on_project("AI Platform")
print("Engineer Annual Salary:", engineer.get_annual_salary())

salesperson = Salesperson("Charlie", 103, 3000, commission_rate=0.05)
salesperson.display_info()
salesperson.calculate_commission(50000)
print("Salesperson Annual Salary (with commission):", salesperson.get_annual_salary(annual_sales=100000))
#######
#5
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def feed_milk(self):
        print(f"{self.name} is feeding milk to its young.")

    def has_fur(self):
        print(f"{self.name} has {self.fur_color} fur.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} meters.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} is swimming in {self.water_type} water.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

mammal = Mammal("Elephant", 10, "gray")
mammal.eat()
mammal.sleep()
mammal.feed_milk()
mammal.has_fur()

bird = Bird("Eagle", 5, 2.5)
bird.eat()
bird.sleep()
bird.fly()
bird.lay_eggs()

fish = Fish("Salmon", 3, "freshwater")
fish.eat()
fish.sleep()
fish.swim()
fish.lay_eggs()
##########
#6
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self):
        print(f"Title: {self.title}, ID: {self.item_id}, Checked Out: {'Yes' if self.is_checked_out else 'No'}")

class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages):
        super().__init__(title, item_id)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}, Pages: {self.num_pages}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration  # in minutes

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Duration: {self.duration} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publication_date):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}, Publication Date: {self.publication_date}")

book = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", 218)
book.display_info()
book.check_out()
book.return_item()

dvd = DVD("Inception", "D002", "Christopher Nolan", 148)
dvd.display_info()
dvd.check_out()

magazine = Magazine("National Geographic", "M003", 42, "October 2024")
magazine.display_info()
magazine.check_out()
magazine.return_item()