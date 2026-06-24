# ==========================================
# Day 3 - For Loop Practice
# Topic: for loop, range(), nested loops,
# break, continue
# Date: 24-06-2026
# ==========================================


# ========== EASY QUESTIONS (1-6) ==========


# ---- QUESTION 1 ----
# Print numbers from 1 to 20 using for loop
for el in range(21):
    print(el)


# ---- QUESTION 2 ----
# Print all even numbers between 1 and 50
# using range() only - no if condition allowed
# Hint: range() has a third argument for step
for el in range(2,50,2):
    print(el)


# ---- QUESTION 3 ----
# Calculate sum of all numbers from 1 to 100
# using for loop
# Do NOT use any formula like n*(n+1)/2
# Actually loop and add
# At the end print the sum
total=0
for el in range(101):
    total=total+el
    print(total)


# ---- QUESTION 4 ----
# User enters a number
# Print its multiplication table using for loop
# Output format:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
n=int(input("Enter a number :"))
i=0
for i in range(1,11):
    print(n,"x",i,"=",n*i)



# ---- QUESTION 5 ----
# Print this pattern using nested for loops
#
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()



# ---- QUESTION 6 ----
# Count how many numbers between 1 and 50
# are divisible by 3 but NOT by 9
# Print each such number and the final count
count=0
for el in range(1,51):
    if(el%3==0 and el%9!=0):
        print(el)
        count+=1
print("total such numbers are :",count) 


# ========== REAL LIFE + ADVANCED (7-13) ==========


# ---- QUESTION 7 ----
# Exam result processor
# You have a list of 8 student marks
# marks = [85, 92, 45, 78, 33, 90, 61, 55]
# Using for loop find:
# 1. How many students passed (pass mark is 60)
# 2. How many students failed
# 3. Highest mark
# 4. Lowest mark
# 5. Class average
# Print all 5 results
marks = [85, 92, 45, 78, 33, 90, 61, 55]
marks = [85, 92, 45, 78, 33, 90, 61, 55]
count=0
count1=0
total=0
noofel=0
for el in marks:
    if(el>=60):
       
        count+=1
    else:
        count1+=1
    total+=el
    noofel+=1
    
print("Total number of passed students :",count)  
print("Total number of failed students :",count1)
print("Total Average of class :",total/noofel)
print(max(marks))
print(min(marks))


# ---- QUESTION 8 ----
# Shopping bill calculator
# A customer buys multiple items
# Keep asking for item name and price
# until customer types "done" as item name
# At the end print:
# - All items with their prices
# - Total bill
# - If total is above 1000 give 10% discount
# - Final amount to pay
# Hint: store items in two lists - names and prices
names = []
prices = []

while True:

    item = input("Enter item name (type done to finish): ")

    if item == "done":
        break

    price = int(input("Enter price: "))

    names.append(item)
    prices.append(price)


total = 0

for p in prices:
    total += p


print("\nItems bought:")

for i in range(len(names)):
    print(names[i], "-", prices[i])


print("Total bill:", total)

if total > 1000:
    discount = total * 0.10
    total = total - discount
    print("10% discount applied")

print("Final amount to pay:", total)



# ---- QUESTION 9 ----
# Attendance tracker
# You have 30 students in a class
# Each student is either Present or Absent
# Generate random attendance using this:
import random
attendance = [random.choice(["Present", "Absent"]) for _ in range(30)]
# Now using for loop find:
# 1. How many students are present
# 2. How many are absent
# 3. Attendance percentage
# 4. If attendance is below 75% print "Low attendance warning"
import random
attendance = [random.choice(["Present", "Absent"]) for _ in range(30)]
countp=0
counta=0
for el in attendance:
    if(el=="Present"):
        countp+=1
    else:
        counta+=1
print(countp) 
print(counta)
print("Average attendace is:",(countp/30)*100)
if ((countp/30)<=0.75):
    print("Low attendance warning")
else:
    print()


# ---- QUESTION 10 ----
# Cricket scorecard
# A batsman plays 10 balls
# runs = [4, 0, 6, 1, 0, 4, 2, 6, 0, 3]
# Using for loop find:
# 1. Total runs scored
# 2. How many dot balls (0 runs)
# 3. How many boundaries (4s)
# 4. How many sixes (6s)
# 5. Strike rate = (total runs / balls played) * 100
# Print full scorecard
runs = [4, 0, 6, 1, 0, 4, 2, 6, 0, 3]
runs = [4, 0, 6, 1, 0, 4, 2, 6, 0, 3]
total=0
dotball=0
boundries=0
sixes=0
for el in runs:
    total+=el
    if(el==0):
        dotball+=1
    if(el==4):
        boundries+=1
    if(el==6):
        sixes+=1
        
print("Total runs scored ;",total)    
print("Total number of dotballs is :",dotball)
print("Total number of boundries is :",boundries)
print("Total number of sixes is :",sixes)
print("Strike rate :", (total/len(runs)*100))


# ---- QUESTION 11 ----
# Salary processor for a small company
# employees = ["Rahul", "Priya", "Tushar", "Anita", "Raj"]
# salaries =  [45000, 62000, 38000, 71000, 55000]
# Using for loop find:
# 1. Total salary bill for the company
# 2. Average salary
# 3. Highest paid employee and their salary
# 4. Lowest paid employee and their salary
# 5. Give 10% raise to anyone earning below 50000
#    and print their new salary

employees = ["Rahul", "Priya", "Tushar", "Anita", "Raj"]
salaries =  [45000, 62000, 38000, 71000, 55000]

total=0 
for el in salaries: 
    total+=el 
    
print("The total salay bill of company :",total)
print("The Average salary :",total/len(salaries))

for el in range(len(salaries)):
    
    highest=max(salaries)
    index=salaries.index(highest)
    lowest=min(salaries)
    index1=salaries.index(lowest)

    if (el<50000):
        newsalary=el*1.1
        print("The new salary of employee is :",newsalary)
print(employees[index],highest)
print(employees[index1],lowest)


# ---- QUESTION 12 ----
# Number pattern - print this exactly
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Then immediately below it print reverse:
#
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
#
# Use only for loops
# write your code here


# ---- QUESTION 13 ----
# Bank statement generator
# A person starts with balance of 50000
# transactions = [2000, -5000, 10000, -3000,
#                 -15000, 8000, -2000, 20000]
# Positive = money deposited
# Negative = money withdrawn
# Using for loop:
# 1. Print each transaction with type
#    (Deposit or Withdrawal) and amount
# 2. Print balance after each transaction
# 3. If balance goes below 1000 at any point
#    print "WARNING: Low balance"
# 4. Print final balance at the end
transactions = [2000, -5000, 10000, -3000,
                -15000, 8000, -2000, 20000]

transactions = [2000, -5000, 10000, -3000,-15000, 8000, -2000,20000]
balance=50000
for el in transactions :
    if(el<0):
        print("Withdrawl:",abs(el))
        balance+=el
        print("The remaining Balance :",balance)
        if(balance<1000):
            print("WARNING: Low balance")
    else:
        print("Deposit",el)
        balance+=el
        print("The remaining Balance :",balance)