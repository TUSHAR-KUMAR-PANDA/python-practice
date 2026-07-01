# ==========================================
# QUESTION 1 - Bank Account using Property
# ==========================================

# Build class BankAccount

# Instance variables:
# owner
# _balance

# Property:
# balance
# → getter returns balance
# → setter:
#     cannot be negative
#     cannot withdraw more than available

# Computed property:
# balance_in_dollars
# (1 dollar = 83 rupees)

# Methods:
# deposit(amount)
# withdraw(amount)
# display()

# Test:
# acc=BankAccount("Tushar",10000)

# print(acc.balance)
# acc.deposit(5000)
# acc.withdraw(3000)
# print(acc.balance_in_dollars)
# acc.balance=-500
# acc.display()

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):

        if value < 0:
            print("Invalid balance")

        else:
            self._balance = value

    @property
    def balance_in_dollars(self):
        return round(self._balance / 83, 2)

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):

        if amount <= self._balance:
            self._balance -= amount

        else:
            print("Insufficient balance")

    def display(self):

        print("Owner:", self.owner)
        print("Balance:", self._balance)


acc = BankAccount("Tushar", 10000)

print(acc.balance)

acc.deposit(5000)

acc.withdraw(3000)

print(acc.balance_in_dollars)

acc.balance = -500

acc.display()



# ==========================================
# QUESTION 2 - Employee Salary System
# ==========================================

# Build class Employee

# Instance variables:
# name
# _salary

# Property:
# salary
# → getter returns salary
# → setter:
#     salary cannot be below 15000

# Computed property:
# annual_salary

# Methods:
# increment(amount)
# display()

# Test:
# emp=Employee("Tushar",50000)

# print(emp.salary)

# emp.increment(10000)

# print(emp.annual_salary)

# emp.salary=10000

# emp.display()



class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 15000:
            print("Salary too low")

        else:
            self._salary = value

    @property
    def annual_salary(self):
        return self._salary * 12

    def increment(self, amount):

        self._salary += amount

    def display(self):

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Annual:", self.annual_salary)


emp = Employee("Tushar", 50000)

print(emp.salary)

emp.increment(10000)

print(emp.annual_salary)

emp.salary = 10000

emp.display()

# ==========================================
# QUESTION 3 - Laptop Battery System
# ==========================================

# Build class Laptop

# Instance variables:
# brand
# _battery

# Property:
# battery
#
# getter:
# → return battery percentage
#
# setter:
# → battery cannot go below 0
# → battery cannot go above 100

# Computed property:
# battery_status
#
# 80–100 → Excellent
# 50–79 → Good
# 20–49 → Low
# 0–19 → Critical

# Methods:
#
# charge(amount)
# → increase battery
#
# use(hours)
# → reduce battery
# → assume 1 hour = 10%
#
# display()

# TEST:

# l1=Laptop("Dell",60)

# print(l1.battery)

# l1.charge(30)

# print(l1.battery_status)

# l1.use(4)

# l1.display()

# l1.battery=150

class Laptop:

    def __init__(self, brand, battery):
        self.brand = brand
        self._battery = battery

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):

        if value < 0 or value > 100:
            print("Invalid battery percentage")

        else:
            self._battery = value

    @property
    def battery_status(self):

        if self._battery >= 80:
            return "Excellent"

        elif self._battery >= 50:
            return "Good"

        elif self._battery >= 20:
            return "Low"

        else:
            return "Critical"

    def charge(self, amount):

        new_battery = self._battery + amount

        if new_battery > 100:
            self._battery = 100

        else:
            self._battery = new_battery

    def use(self, hours):

        used = hours * 10

        if self._battery - used < 0:
            self._battery = 0

        else:
            self._battery -= used

    def display(self):

        print("Brand:", self.brand)
        print("Battery:", self.battery, "%")
        print("Status:", self.battery_status)


l1 = Laptop("Dell", 60)

print(l1.battery)

l1.charge(30)

print(l1.battery_status)

l1.use(4)

l1.display()

l1.battery = 150

l1.display()

