#==========================================
#REVISION SHEET
#FUNCTIONS+OOP+INHERITANCE+DUNDER+PROPERTY
#==========================================


#==========================================
#QUESTION 1 - FUNCTIONS REVISION
#==========================================

#Build Student Report Generator

#Functions:
#calculate_average(marks)
#-> returns average

#get_grade(avg)
#-> A (90+)
#-> B (80+)
#-> C (70+)
#-> F (<70)

#is_promoted(avg)
#-> True if avg>=60

#generate_report(name,*marks)
#-> uses all above functions
#-> prints full report

#create_students(**kwargs)
#-> accepts:
#student_name=marks_list
#-> prints report for every student

#Test:

#create_students(
#Tushar=[85,92,78,90],
#Rahul=[65,70,60,55],
#Priya=[98,95,96,99]
#)
def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "F"


def is_promoted(avg):
    return avg >= 60


def generate_report(name, *marks):
    average = calculate_average(marks)
    grade = get_grade(average)
    promoted = is_promoted(average)

    print("---------------------------")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Promoted:", promoted)
    print("---------------------------")


def create_students(**kwargs):
    for name, marks in kwargs.items():
        generate_report(name, *marks)


create_students(
    Tushar=[85, 92, 78, 90],
    Rahul=[65, 70, 60, 55],
    Priya=[98, 95, 96, 99]
)

#==========================================
#QUESTION 2 - OOP REVISION
#==========================================

#Build class BankAccount

#Class Variables:
#bank_name
#total_accounts

#Instance Variables:
#owner
#balance
#transactions

#Methods:
#deposit(amount)
#withdraw(amount)
#transfer(other_account,amount)
#show_statement()
#display_info()

#Create 3 accounts
#Test all methods
class BankAccount:

    bank_name = "SBI"
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.transactions.append(f"Deposited Rs {amount}")
            print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew Rs {amount}")
            print("Withdrawal successful")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            other_account.balance += amount

            self.transactions.append(
                f"Transferred Rs {amount} to {other_account.owner}"
            )

            other_account.transactions.append(
                f"Received Rs {amount} from {self.owner}"
            )

            print("Transfer successful")

    def show_statement(self):
        print("\n----- Statement -----")
        print("Account Holder:", self.owner)

        if len(self.transactions) == 0:
            print("No transactions")
        else:
            for transaction in self.transactions:
                print(transaction)

        print("Current Balance:", self.balance)

    def display_info(self):
        print("\n----- Account Info -----")
        print("Bank:", BankAccount.bank_name)
        print("Owner:", self.owner)
        print("Balance:", self.balance)


acc1 = BankAccount("Tushar", 10000)
acc2 = BankAccount("Rahul", 8000)
acc3 = BankAccount("Priya", 12000)

acc1.deposit(2000)
acc1.withdraw(1500)
acc1.transfer(acc2, 3000)

acc1.display_info()
acc2.display_info()
acc3.display_info()

acc1.show_statement()
acc2.show_statement()
acc3.show_statement()

print("Total Accounts:", BankAccount.total_accounts)


#==========================================
#QUESTION 3 - INHERITANCE REVISION
#==========================================

#Parent Class:
#Employee

#Variables:
#name
#salary

#Methods:
#display_info()
#work()

#Child Class 1:
#Developer

#Extra Variable:
#programming_language

#Override:
#work()

#Child Class 2:
#DataScientist

#Extra Variable:
#specialization

#Override:
#work()

#Child Class 3:
#Manager

#Extra Variable:
#team_size

#Override:
#work()

#Create objects
#Test all classes

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def work(self):
        print(self.name, "is working.")


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        print(self.name, "is developing software using", self.programming_language)


class DataScientist(Employee):

    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization = specialization

    def work(self):
        print(self.name, "is working on", self.specialization)


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(self.name, "is managing a team of", self.team_size, "employees")


d1 = Developer("Tushar", 70000, "Python")
ds1 = DataScientist("Rahul", 90000, "Machine Learning")
m1 = Manager("Priya", 120000, 15)

d1.display_info()
d1.work()

print()

ds1.display_info()
ds1.work()

print()

m1.display_info()
m1.work()

#==========================================
#QUESTION 4 - DUNDER METHODS REVISION
#==========================================

#Build class Book

#Variables:
#title
#pages

#Dunder Methods:
#__str__
#__repr__
#__len__
#-> returns pages

#__add__
#book1+book2
#-> returns total pages

#__eq__
#__gt__
#__lt__

#Test:

#b1=Book("Python",300)
#b2=Book("ML",450)

#print(b1)
#print(repr(b1))
#print(len(b1))
#print(b1+b2)
#print(b1==b2)
#print(b1>b2)
#print(b1<b2)

class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages


b1 = Book("Python", 300)
b2 = Book("Machine Learning", 450)
b3 = Book("Data Science", 300)

print(b1)
print(repr(b1))

print(len(b1))

print(b1 + b2)

print(b1 == b2)
print(b1 == b3)

print(b1 > b2)
print(b1 < b2)

#==========================================
#QUESTION 5 - PROPERTY DECORATOR REVISION
#==========================================

#Build class Student
#Variables:
#name
#_cgpa
#Property:
#cgpa
#setter:
#allow only values 0 to 10
#Computed Property:
#grade
#9+ -> A
#8+ -> B
#7+ -> C
#else -> F
#Methods:
#display()
#Test:
#s1=Student("Tushar",6.31)
#print(s1.cgpa)
#print(s1.grade)
#s1.cgpa=8.7
#print(s1.grade)
#s1.cgpa=12
#s1.display()

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self._cgpa = cgpa

    @property
    def cgpa(self):
        return self._cgpa

    @cgpa.setter
    def cgpa(self, value):
        if 0 <= value <= 10:
            self._cgpa = value
        else:
            print("Invalid CGPA")

    @property
    def grade(self):
        if self._cgpa >= 9:
            return "A"
        elif self._cgpa >= 8:
            return "B"
        elif self._cgpa >= 7:
            return "C"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("CGPA:", self.cgpa)
        print("Grade:", self.grade)


s1 = Student("Tushar", 6.31)

print(s1.cgpa)
print(s1.grade)

s1.cgpa = 8.7

print(s1.grade)

s1.cgpa = 12

s1.display()