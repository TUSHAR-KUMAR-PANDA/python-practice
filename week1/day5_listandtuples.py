# ==========================================
# Day 5 - Lists and Tuples Practice
# Topic: lists, tuples, indexing, slicing,
# list methods, for loops with lists
# Date: 25-06-2026
# ==========================================


# ========== EASY QUESTIONS (1-6) ==========


# ---- QUESTION 1 ----
# Create a list of 5 of your favourite movies
# Print the first movie
# Print the last movie
# Print the middle movie
# Print total number of movies using len()
movies=["13 ghost","pk","got","hod","vikings"]
print(movies)
print(movies[0])
print(movies[4])
print(movies[2])
print(len(movies))


# ---- QUESTION 2 ----
# You have this list of numbers
numbers = [10, 25, 3, 47, 8, 92, 15, 63]
# Print the largest number without using max()
# Print the smallest number without using min()
numbers = [10, 25, 3, 47, 8, 92, 15, 63]
numbers.sort()
print("The smallest nummber is :",numbers[0])
numbers.reverse()
print("The laargest number is :",numbers[0])


# ---- QUESTION 3 ----
# Create a list of numbers from 1 to 10
# using a for loop and append()
# Do NOT write the list manually
# Then print the list
# Then print it in reverse using reverse()
list=[]
for el in range(1,11):
    list.append(el)
print(list)



# ---- QUESTION 4 ----
# You have this list
fruits = ["apple", "banana", "mango",
          "orange", "grapes", "banana", "mango"]
# 1. Print total number of fruits
# 2. Print how many times "banana" appears
# 3. Remove the first "banana" from the list
# 4. Add "watermelon" at the end
# 5. Insert "kiwi" at position 2
# 6. Print the final list
fruits = ["apple", "banana", "mango", "orange", "grapes", "banana", "mango"]
print("Total number of elements :",len(fruits))
fruits.remove("banana")
fruits.append("watermelon")
fruits.insert(2,"kiwi")
print("fruits =",fruits)


# ---- QUESTION 5 ----
# Slicing practice
student_names = ["Tushar", "Rahul", "Priya",
                 "Anita", "Raj", "Neha", "Vikram"]
# 1. Print first 3 students
# 2. Print last 3 students
# 3. Print students from index 2 to 5
# 4. Print every alternate student
# 5. Print the list in reverse using slicing
print("The first 3 student name are:",student_names[0:3])
print("The last 3 student names:",student_names[-4:-1])
print("The students from indx 2 to 5:",student_names[2:6])
print("Alternate Students :",student_names[::2])
print("Reverse of an element :",student_names[::-1])


# ---- QUESTION 6 ----
# Tuple basics
# Create a tuple with your personal info
# (name, age, city, college, branch)
# Print each item using indexing
# Try to change one value and see what error you get
# Write the error as a comment in your code
tuple=("Tushar",20,"Balasore","KIIT","cse")
print(tuple[0])
print(tuple[1])
print(tuple[2])
tuple[0]="Ram"
print(tuple[0])
#It means tuples are immutable and if a tuple is already defined and later on we decide to change the value at some index we just cant randomly define and do that 

# ========== REAL WORLD + ADVANCED (7-13) ==========


# ---- QUESTION 7 ----
# Student marks analyser
marks = [78, 92, 45, 88, 61, 73, 55, 94, 38, 82]
# Using for loop find:
# 1. Total marks
# 2. Average marks
# 3. Highest marks
# 4. Lowest marks
# 5. How many students passed (pass mark 60)
# 6. How many failed
# 7. Print a grade for each mark
#    A = 90 and above
#    B = 75 to 89
#    C = 60 to 74
#    F = below 60

marks = [78, 92, 45, 88, 61, 73, 55, 94, 38, 82]
total=0
failed=0
passed=0
for el in marks:
    total+=el
    if(el<60):
        failed+=1
    else:
        passed+=1
            
print("The total mark is :",total) 
print("The average mark is :", total/len(marks))
print("The number of students failed:",failed)
print("The number of students passed:",passed)

for el in marks:
    if(el>=90):
        print("GRADE A -",el)
    elif(75<=el<=89):
        print("GRADE B -",el)
    elif(60<=el<=74):
        print("GRADE C - ",el)
    else :
        print("GRADE F -",el)



# ---- QUESTION 8 ----
# Shopping cart system
# Start with empty cart
cart = []
prices = []
# Keep asking user for item name and price
# If user types "done" stop asking
# After done:
# 1. Print all items with prices neatly
# 2. Print total bill
# 3. If bill above 500 apply 5% discount
# 4. If bill above 1000 apply 10% discount
# 5. If bill above 2000 apply 15% discount
# 6. Print final amount after discount
cart = []
prices = []


county=0

while True :
    x=input("Enter the item (If you want to exit type done):")
    if(x=="done"):
        print("shopping completed")
        break
    cart.append(x)
    
    y=int(input("Enter the price of items :"))
    prices.append(y)
    county+=y
    
for i in range(len(cart)):
    print(cart[i],"=",prices[i])
print("Total billing amount:",county)

if (county>500 and county<1000):
    print("Amount after discount:",county-(county*0.05))
elif(county>1000 and county<2000):
    print("Amount after discount:",county-(county*0.1))
elif(county>2000):
    print("Amount after discount:",county-(county*0.15))


# ---- QUESTION 9 ----
# Temperature converter and analyser
# Daily temperatures for a week in Celsius
temps_celsius = [38, 35, 40, 33, 37, 42, 36]
days = ["Mon", "Tue", "Wed",
        "Thu", "Fri", "Sat", "Sun"]
# 1. Convert all temperatures to Fahrenheit
#    Formula: F = C * 9/5 + 32
#    Store in a new list temps_fahrenheit
# 2. Print each day with both C and F temperature
# 3. Find hottest day and temperature
# 4. Find coolest day and temperature
# 5. Find average temperature for the week
# 6. Count how many days were above 37 degrees
temps_celsius = [38, 35, 40, 33, 37, 42, 36]
days = ["Mon", "Tue", "Wed","Thu", "Fri", "Sat", "Sun"]
temps_farenhite=[]
total=0
above37=0

for el in temps_celsius:
    far=el* 9/5 + 32
    temps_farenhite.append(far)
    total+=el
    if(el>37):
        above37+=1
    
print(temps_farenhite)    
    
for i in range(len(temps_celsius)):
    print(days[i],"=",temps_farenhite[i],"~F","=",temps_celsius[i],"`C")
hottest=max(temps_celsius)
index=temps_celsius.index(hottest)
coolest=min(temps_celsius)
index1=temps_celsius.index(coolest)
print("The hottest day :",days[index])
print("The coolest day :",days[index1])
print("The average temprature is :",total/len(temps_celsius))
print("The no of days with tempt above 37 is :",above37)


# ---- QUESTION 10 ----
# Duplicate remover
numbers = [1, 2, 3, 2, 4, 3, 5,1, 6, 4, 7, 5, 8, 2, 9]
# Remove all duplicates from this list
# Keep only unique numbers
# Maintain the original order
# Do NOT use set()
# Use only list methods and for loop
# Print original list and cleaned list
# write your code here
numbers = [1, 2, 3, 2, 4, 3, 5,1, 6, 4, 7, 5, 8, 2, 9]
new_numbers=[]
for el in numbers:
    if(el in new_numbers):
        continue
        
    else:
        new_numbers.append(el)
print(new_numbers)   

# ---- QUESTION 11 ----
# Cricket team selector
# You have player names and their scores
players = ["Rohit", "Virat", "Dhoni",
           "Bumrah", "Jadeja", "Hardik",
           "Shami", "KL Rahul", "Pant",
           "Ashwin", "Siraj"]
scores =  [85, 92, 78, 65, 70,
           88, 60, 75, 82, 68, 55]
# 1. Find top 5 players by score
#    Print their names and scores
# 2. Find players scoring below 70
#    These players are dropped from team
#    Print dropped players
# 3. Calculate team average score
# 4. Find the player with highest score
#    Print "Captain: playername with score X"
# Hint: you can use sorted() or sort()
#       to arrange scores
for i in range(len(scores)):
    for j in range(i+1, len(scores)):

        if scores[i] < scores[j]:

            scores[i], scores[j] = scores[j], scores[i]

            players[i], players[j] = players[j], players[i]

print("Top 5 Players:")  
for i in range(5):
    print(players[i], "-", scores[i])
  

# ---- QUESTION 12 ----
# Tuple coordinate system
# You have locations as tuples
locations = [
    ("Home", 20.2961, 85.8245),
    ("College", 20.3549, 85.8198),
    ("Market", 20.2700, 85.8388),
    ("Hospital", 20.3200, 85.8150),
    ("Railway Station", 20.2647, 85.8349)
]
# Each tuple has (place_name, latitude, longitude)
# 1. Print all location names
# 2. Print name and coordinates of each place neatly
# 3. Try to change the latitude of Home
#    Write the error as a comment - explains why tuples
#    are used for coordinates (they should not change)
# 4. Find which location has highest latitude
highest=locations[0]
print("All the location names:")
for el in locations:
    print(el[0])
print("Places and their coordinates:")    
for el in locations :
    print(el[0],"Coordinates are:",el[1],"and",el[2])
for el in locations:
    if(el[1]>highest[1]):
        highest=el
print(highest[0])  


# ---- QUESTION 13 ----
# Exam seating arrangement
# You have 20 students
# They need to be split into 4 rows of 5
# Generate the seating using slicing
students = [
    "Tushar", "Rahul", "Priya", "Anita", "Raj",
    "Neha", "Vikram", "Pooja", "Arjun", "Sneha",
    "Kiran", "Mohit", "Divya", "Suresh", "Kavya",
    "Rohit", "Meena", "Ajay", "Sita", "Deepak"
]
# 1. Split into 4 rows using slicing
#    Row 1: students 1-5
#    Row 2: students 6-10
#    Row 3: students 11-15
#    Row 4: students 16-20
# 2. Print each row neatly
#    Row 1: Tushar, Rahul, Priya, Anita, Raj
# 3. Find which row Tushar is in
# 4. Swap row 1 and row 3
#    Print new arrangement
students = [
    "Tushar", "Rahul", "Priya", "Anita", "Raj",
    "Neha", "Vikram", "Pooja", "Arjun", "Sneha",
    "Kiran", "Mohit", "Divya", "Suresh", "Kavya",
    "Rohit", "Meena", "Ajay", "Sita", "Deepak"
]

row = 1

for el in range(0, len(students), 5):
    print("Row", row, ":", students[el:el+5])
    row += 1


for el in range(0, len(students), 5):

    if "Tushar" in students[el:el+5]:

        print("Tushar is in Row", (el//5)+1)


row1 = students[0:5]
row3 = students[10:15]

students[0:5] = row3
students[10:15] = row1


print("\nNew Arrangement:")

row = 1

for el in range(0, len(students), 5):
    print("Row", row, ":", students[el:el+5])
    row += 1
    