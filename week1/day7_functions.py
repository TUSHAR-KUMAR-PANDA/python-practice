# ==========================================
# Day 7 - Functions Practice
# Topic: def, parameters, return, default
# arguments, *args, **kwargs, scope
# Date: 27-06-2026
# ==========================================


# ========== EASY QUESTIONS (1-5) ==========


# ---- QUESTION 1 ----
# Write a function called greet
# It takes a name as parameter
# It prints "Hello [name], welcome to Python!"
# Call it 3 times with different names
def greet(a):
    
    print("Hello",a," welcome to Python!")
    return a 
    
greet("tushar")   
greet("anil")
greet("soham")


# ---- QUESTION 2 ----
# Write a function called calculate
# It takes two numbers and an operator as parameters
# Operator can be +, -, *, /
# It RETURNS the result (don't just print)
# Call it and print the returned result
# Handle division by zero with a message
def calculate(a,b,operator):
    if (operator=="+"):
        return a+b
    if (operator=="/"):
        if(a==0 or b==0):
            print("NOT DEFINED ")
            return
    if (operator=="-"):
        return a-b
    if (operator=="*"):
        return a*b
calculate(2,4,"+")    
print(calculate(2,4,"+"))  
    


# ---- QUESTION 3 ----
# Write a function called is_even
# Takes a number, RETURNS True if even, False if odd
# Write another function called is_prime
# Takes a number, RETURNS True if prime, False if not
# Test both functions with 5 different numbers each

def is_even(n):
    if(n%2==0):
        print("TRUE")
        
    else:
        print("FALSE")
print(is_even(3))  


def is_prime(n):
    if(n<2):
        print("FALSE")
    for i in range(2,n):
        if(n%i==0):
            print("FALSE")
        else:
            print("TRUE")
            
        
is_prime(3)  

# ---- QUESTION 4 ----
# Write a function with DEFAULT parameters
# Function called introduce
# Parameters: name, age, city="Bhubaneswar", language="Python"
# Prints a self introduction
# Call it:
# 1. With only name and age
# 2. With name, age and city
# 3. With all four parameters
# write your code here


# ---- QUESTION 5 ----
# Write a function called list_stats
# Takes a list of numbers as parameter
# RETURNS a tuple containing:
# (minimum, maximum, sum, average)
# Test it with marks = [85, 92, 45, 78, 33, 90, 61, 55]
# Unpack the returned tuple and print each value
# write your code here


# ========== INTERMEDIATE TO ADVANCED (6-13) ==========


# ---- QUESTION 6 ----
# *args practice
# Write a function called total_bill
# It should accept any number of item prices
# Calculate and return the total
# Call it with 2 items, then 4 items, then 6 items
# write your code here


# ---- QUESTION 7 ----
# **kwargs practice
# Write a function called create_profile
# It accepts any number of keyword arguments
# Prints each key and value neatly
# Example call:
# create_profile(name="Tushar", age=20,
#                college="KIIT", cgpa=6.31)
# write your code here


# ---- QUESTION 8 ----
# Recursive function
# Write a function called factorial
# Takes a number n
# Returns n! (factorial)
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Use recursion - function calling itself
# Also print the factorial of numbers 1 to 10

def factorial(n):
    if (n==1):
        return 1
    return n*factorial(n-1)
    
for i in range(1, 11):
    print(f"factorial({i}) =", factorial(i))


# ---- QUESTION 9 ----
# Write a function called fibonacci
# Takes a number n
# Returns the nth fibonacci number
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
# fibonacci(1) = 0
# fibonacci(2) = 1
# fibonacci(7) = 8
# Use recursion
# Print first 10 fibonacci numbers
def fibonacci(n):
    # Base case
    if(n==1):
        return 1
    if(n==0):
        return 0
    # recursion case
    return fibonacci(n-1)+fibonacci(n-2)
    
    
for n in range(1,11):
    print(fibonacci(n))


# ---- QUESTION 10 ----
# Scope practice
x = 100  # global variable

def scope_test():
    x = 50  # local variable
    print("Inside function x:", x)

scope_test()
print("Outside function x:", x)

# Now write a function that MODIFIES the global x
# using the global keyword
x = 100   # global variable


def scope_test():
    x = 50
    print("Inside function x:", x)


scope_test()
print("Outside function x:", x)


# Modify global variable

def modify_global():
    global x
    x = 500


modify_global()

print("Modified global x:", x)

# ---- QUESTION 11 ----
# Real world - ATM with functions
# Break the ATM problem into functions:
# 1. check_balance(balance) - prints current balance
# 2. deposit(balance, amount) - returns new balance after deposit
# 3. withdraw(balance, amount) - returns new balance if valid
#                              - returns -1 if invalid
# 4. is_valid_withdrawal(balance, amount) - returns True or False
# Build a simple ATM loop using these functions
balance = 10000
balance = 10000


def check_balance(balance):
    print("Current Balance:", balance)


def deposit(balance, amount):
    return balance + amount


def is_valid_withdrawal(balance, amount):
    return amount <= balance


def withdraw(balance, amount):
    if is_valid_withdrawal(balance, amount):
        return balance - amount
    else:
        return -1


while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance = deposit(balance, amount)
        print("Deposit Successful")

    elif choice == "3":
        amount = int(input("Enter amount: "))

        new_balance = withdraw(balance, amount)

        if new_balance == -1:
            print("Insufficient Balance")

        else:
            balance = new_balance
            print("Withdrawal Successful")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")


# ---- QUESTION 12 ----
# Function that returns a function
# Write a function called multiplier
# It takes a number n as parameter
# It RETURNS a function that multiplies any number by n
# Example:
# double = multiplier(2)
# triple = multiplier(3)
# print(double(5))   # Output: 10
# print(triple(5))   # Output: 15
# This is called a closure - important concept
def multiplier(n):
    def number(m):
        return n*m
    return number
    
double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5)) 


# ---- QUESTION 13 ----
# Real world - Student report generator
# Write these functions:
# 1. calculate_average(marks) - returns average
# 2. get_grade(average) - returns grade A/B/C/F
# 3. is_promoted(average) - returns True if average >= 60
# 4. generate_report(name, marks) - uses all above functions
#    prints complete report card for a student
#
# Test with these students:
students = {
    "Tushar": [85, 92, 78, 90, 88],
    "Rahul": [72, 68, 75, 80, 71],
    "Priya": [95, 98, 92, 96, 94],
    "Anita": [55, 60, 58, 62, 57],
    "Raj":   [40, 45, 38, 50, 42]
}
# Call generate_report for each student
students = {
    "Tushar": [85, 92, 78, 90, 88],
    "Rahul": [72, 68, 75, 80, 71],
    "Priya": [95, 98, 92, 96, 94],
    "Anita": [55, 60, 58, 62, 57],
    "Raj":   [40, 45, 38, 50, 42]
}
# Call generate_report for each student

def calculate_average(marks):
    total=0
    for el in marks:
        total+=el
    average=total/len(marks) 
    return average


print(calculate_average([85, 92, 78, 90, 88]))      

def get_grade(average):
    if(average>=90):
        return "A"
    elif(80<=average<90):
        return "B"
    elif(70<=average<80):
        return "C" 
    else:
        return "F"

print(get_grade(86.6))  


def is_promoted(average):
    if(average>=60):
        return "True"
    else:
        return "False"
        
print(is_promoted(54))


def generate_report(name):
    if name not in students:
        print("Student not found")
        return

    marks = students[name]
    avg = calculate_average(marks)
    grade = get_grade(avg)
    promoted = is_promoted(avg)

    print("Name:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)
    print("Promoted:", promoted)
    print("----------------------")


for student in students:
    generate_report(student)

