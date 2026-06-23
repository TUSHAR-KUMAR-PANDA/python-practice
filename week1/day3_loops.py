# ==========================================
# Day 3 - While Loop Practice
# Topic: while loop, break, continue
# Date: 23-06-2026
# ==========================================


# ========== EASY QUESTIONS (1-6) ==========


# ---- QUESTION 1 ----
# Print numbers from 1 to 10 using while loop
i=1
while i<=10:
    print(i)
    i+=1



# ---- QUESTION 2 ----
# Print numbers from 10 down to 1 using while loop
# Then print "DONE!"
i = 10
while i>=1:
    print(i)
    i-=1


# ---- QUESTION 3 ----
# Keep asking user to enter a number
# Stop when user enters 0
# Print how many numbers they entered
# Do not count the 0
n=int(input("enter the number :"))
count = 0
while n!=0:
    print(n)
    count+=1
    n=int(input("enter number again:"))
while n==0:
    print("ENDED")
    break
print("total number of times you entered the numbers :", count)    




# ---- QUESTION 4 ----
# Calculate sum of digits of a number
# Example: 1234 → 1+2+3+4 = 10
# Use while loop and modulo #=== IMP === if the number is like 1234 then 1234%10=4, this will give the largest number in the number and then 1234//10=123 this will chop the previous largest number and similarly we have to do this till we get 0
# Do NOT convert to string

n=int(input("Enter the number:"))
total=0
while n!=0:
    a=n%10
    n=n//10
    total=total+a
while n==0:
    break
print("the total sum of the digits are :", total)


# ---- QUESTION 5 ----
# Print multiplication table of a number
# using while loop
# User enters the number
# Print table from 1 to 10
i=1
n=int(input("Enter the number :"))
while i<=10:
    print(n*i)
    i+=1




# ---- QUESTION 11 ----
# ATM simulation
# Balance is 10000
# Keep asking user for withdrawal amount
# Rules:
# Must be greater than 0
# Must be multiple of 100
# Cannot exceed balance
# Cannot exceed 20000 in one transaction
# If user enters -1 exit and show final balance
# Show balance after every successful withdrawal
Balance=100000
WA=int(input("Enter the Withdrawl Amount :"))
while WA>0 :
    if (WA%100==0):
        if(WA<Balance):
            if(WA<20000):
                print("Amount Withdrawl successful:",WA)
                print(Balance-WA)
                WA=int(input("Enter the Withdrawl Amount :"))
while WA==-1:
    print("Exiting Withdrawl")
    break
    print("")


# ---- QUESTION 12 ----
# Collatz Conjecture
# Start with any positive number
# If even divide by 2
# If odd multiply by 3 and add 1
# Keep doing this until you reach 1
# Print every step
# Count how many steps it takes to reach 1
# Example: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
n=int(input("ENTER A POSITIVE NUMBER :"))
count=0
while n!=1:
    if(n%2==0):
        n=n//2
        print(n)
        
    elif(n%2!=0):
        n=n*3+1
        print(n)
    count+=1    
while n==1:
    
    print("total steps :",count)
    break


# ---- QUESTION 13 ----
# Simple login system with limited attempts
# Correct username is "tushar"
# Correct password is "kiit2026"
# User gets maximum 3 attempts
# If correct print "Login successful. Welcome Tushar"
# If wrong print "Wrong credentials. X attempts remaining"
# If all 3 attempts used print "Account locked"
# Use while loop and break
max_attempts = 3
username="tushar"
password="kiit2026"
username=input("enter the name:")
password=input("enter the password :")
count=0
while count<=3:
    if(username == "tushar" and password=="kiit2026"):
        print("Login successful. Welcome Tushar")
    
    else:
        count+=1
        print("Wrong credentials.",3-count ,"attempts left")
        username=input("enter the name:")
        password=input("enter the password :")

        

