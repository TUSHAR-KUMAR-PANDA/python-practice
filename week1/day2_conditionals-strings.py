# ==========================================
# Day 2 - Conditional Statements Practice
# Topic: if, elif, else, nested conditions
# Date: 22-06-2026
# ==========================================

# ---- QUESTION 1 ----
# Check if a number is positive, negative or zero
num=int(input("ENTER THE NUMBER :"))
if(num>0):
    print("THE ENTERED NUMBER IS POSITIVE")
elif(num<0):
    print("the number is negative ")
else:
    print("the number is 0")   

# ---- QUESTION 2 ----
# Check if a number is even or odd
num=int(input("enter the number:"))
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")



# ---- QUESTION 3 ----
# Grade calculator
# 90 and above = A
# 80 to 89 = B
# 70 to 79 = C
# 60 to 69 = D
# below 60 = F
marks=int(input("enter your marks "))
if(marks>=90):
    print("GRADE A ")
elif(80<=marks<=89):
    print("GRADE B")
elif(70<=marks<=79):
    print("GRADE C")
elif(60<=marks<=69):
    print("GRADE D")
else:
    print("GRADE F")


# ---- QUESTION 4 ----
# Find the largest number among three numbers
a = 10
b = 25
c = 17
if(a>b and a>c):
    print("a is the largest number ")
elif (b>a and b>c):
    print("b is the greater number ")
elif(c>a and c>b):
    print("c is the greater number ")
else:
    print("all the number are same ")           

# ---- QUESTION 5 ----
# Check if a person can vote
# Age must be 18 or above to vote
age=int(input("enter your age"))
if(age>=18):
    print("you are eligible to vote ")
else:
    print("you are not eligible to vote ")    

# ---- QUESTION 6 ----
# Check if a year is a leap year
# A year is leap if:
# divisible by 4
# but if divisible by 100 it must also be divisible by 400
year=int(input("enter the year :"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("the year is leap year ")
        else:
            print("the year is not leap year")
    else:
        print("the year is a leap year")
else:
    print("the year is not a leap year")                    


# ---- QUESTION 7 ----
# Simple calculator
# Take two numbers and an operator (+, -, *, /)
# Print the result based on operator

num1=int(input("enter the number:"))
num2=int(input("enter the number :"))
op1="+"
op2="-"
op3="*"
op4="/"
operator=input("enter the operator :")
if(operator==op1):
    print(num1+num2)
elif(operator==op2):
    print(num1-num2)
elif(operator==op3):
    print(num1*num2)
elif(operator==op4):
    print(num1/num2)            

# ---- QUESTION 8 ----
# Check if a number is divisible by both 3 and 5
# or only by 3
# or only by 5
# or neither
num =int(input("enter the number :"))
if(num%3==0 and num%5==0):
    print("it is divisible by both 3 and 5")
elif(num%3==0):
    print("it is divisible by 3")
elif(num%5==0):
    print("it is divisible by 5")
else:
    print("error or not divisible by any")    


# ---- QUESTION 9 ----
# Ticket price calculator
# Children below 5 = free
# Age 5 to 12 = 100 rupees
# Age 13 to 17 = 200 rupees
# Age 18 and above = 300 rupees
age=int(input("enter your age :"))
if(age<5):
    print("your ticket is free")
elif(5<=age<=12):
    print("your ticket price is 100 rupees")
elif(13<=age<=17):
    print("your ticket price is 200 rupees")
else:
    print("your ticket price is 300 rupees")





# ---- QUESTION 10 ----
# Check if a triangle is valid
# A triangle is valid if sum of any two sides
# is greater than the third side
s1=int(input("enter the first side of the triangle"))
s2=int(input("enter the second side of the triangle"))
s3=int(input("enter the third side of the triangle"))
if(s1+s2>s3):
    print("VALID")
elif(s2+s3>s1):
    print("VALID")
elif(s1+s3>s2):
    print("VALID")
else:
    print("NOT VALID ")



# ---- QUESTION 11 ----
# BMI calculator
# Underweight = below 18.5
# Normal = 18.5 to 24.9
# Overweight = 25 to 29.9
# Obese = 30 and above

w=int(input("enter your weight i kg:"))
h=int(input("enter your height in m :"))
bmi=w/(h*h)
if(bmi<18.5):
    print("UNDERWEIGHT")
elif(18.5<=bmi<=24.9):
    print("NORMAL")
elif(25<=bmi<=29.9):
    print("OVER WEIGHT")
else:
    print("OBESE")
# ---- QUESTION 12 ----
# Login system
# Check if username AND password are both correct
# username should be "tushar"
# password should be "kiit2026"
# if both correct print "Login successful"
# if username wrong print "Username not found"
# if password wrong print "Wrong password"
entered_username = "tushar"
entered_password = "kiit2026"
username=input("Enter the username :")
password=input("Enter the password :")
if(entered_username==username and entered_password==password):
    print("LOGIN SUCCESSFUL")
elif(entered_username!=username):
    print("USERNAME NOT FOUND ")
else:
    print("WRONG PASSWORD")

# ==========================================
# Day 2 - Conditionals Advanced Practice
# Topic: Nested conditions, logical operators,
# complex real world problems
# Date: 22-06-2026
# ==========================================

# ---- QUESTION 1 ----
# FizzBuzz but harder
# If number is divisible by 3 print "Fizz"
# If divisible by 5 print "Buzz"
# If divisible by both 3 and 5 print "FizzBuzz"
# If divisible by 7 print "Jazzy"
# If divisible by both 3 and 7 print "FizzJazzy"
# If divisible by both 5 and 7 print "BuzzJazzy"
# If divisible by 3, 5 and 7 print "FizzBuzzJazzy"
# Otherwise print the number itself
num=int(input("enter the number :"))
if(num%3==0):
    print("Fizz")
elif(num%5==0):
    print("Buzz")
elif(num%3==0 and num%5==0):
    print("FizzBuzz")
elif(num%7==0):
    print("Jazzy")
elif(num%3==0 and num%7==0):
    print("FizzJazzy")
elif(num%5==0 and num%7==0):
    print("BuzzJazzy")
elif(num%3==0 and num%5==0 and num%7==0):
    print("FizzBuzzJazzy")
else:
    print(num)

# ---- QUESTION 2 ----
# Bank loan eligibility
# Person is eligible for loan ONLY if ALL conditions are true:
# Age is between 21 and 60
# Monthly salary is above 25000
# Credit score is above 700
# No existing loans (existing_loan = False)
age=int(input("enter your age :"))
salary=int(input("enter your salary :"))
creditscore=int(input("enter your creditscore :"))
existing_loan=False
if (21<age<60 and salary>25000 and creditscore>700 and existing_loan==False):
    print("You are applicable for the loan")
else:
    print("You are not applicable for the Loan")



# ---- QUESTION 3 ----
# Rock Paper Scissors result
# player1 and player2 both choose rock/paper/scissors
# Print who wins or if it is a draw
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
p1=input("enter your choice:")
p2=input("enter your choice:")
Rock="Rock"
Scissors="Scissors"
Paper="Paper"
if(p1==Rock and p2==Scissors):
    print("Player 1 wins")
elif(p1==Rock and p2==Paper):
    print("player 2 wins")
elif(p1==Paper and p2==Scissors):
    print("player 2 wins")
elif(p1==Paper and p2==Rock):
    print("player 1 wins")
elif(p1==Scissors and p2==Paper):
    print("player 1wins")
elif(p1==Scissors and p2==Rock):
    print("player 2 wins")
elif(p1==p2):
    print("it is a draw")        

# ---- QUESTION 11 ----
# ATM machine simulation
# User has a balance and enters withdrawal amount
# Conditions to check in order:
# 1. Amount must be greater than 0
# 2. Amount must be a multiple of 100
# 3. Amount must not exceed 20000 in one transaction
# 4. Amount must not exceed current balance
# 5. After withdrawal if balance goes below 1000
#    charge 50 rupees maintenance fee
# Print success or exact reason for failure
balance=int(input("enter your balance"))
WA=int(input("enter your withdrawl amount :"))
if(WA<=0):
    print("Invalid amount . The amount must be greater then 0")
elif(WA%100!=0):
    print("The WA must be a multiple of 100")
elif(WA>20000):
    print("The WA muat be less then 20000")
elif(WA<balance):
    print("Insufficient Balance")
else:
    print("THE WITHDRAWL IS SUCCESSFUL")
    print("The withdrawl amount is :",WA)
    
    newbalance=balance-WA
    if(newbalance<1000):
        print("50 RS WILL BE DEDUCTED FOR MAINTENCE CHARGE. THE  NEW AMOUNT IS :",newbalance-50)
    else:
        print(newbalance)


                    