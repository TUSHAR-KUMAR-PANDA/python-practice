# ==========================================
# Day 6 - Sets and Dictionaries Practice
# Topic: sets, dictionaries, methods,
# real world problems
# Date: 26-06-2026
# ==========================================


# ========== SETS - EASY (1-4) ==========


# ---- QUESTION 1 ----
# Create a set of 5 favourite programming languages
# Try adding a duplicate and see what happens
# Add a new language using add()
# Remove one language using remove()
# Print final set and its length



# ---- QUESTION 2 ----
# You have two sets of students
# who passed different subjects
passed_maths = {"Tushar", "Rahul", "Priya",
                "Anita", "Raj", "Neha"}
passed_science = {"Rahul", "Priya", "Vikram",
                  "Anita", "Deepak"}
# Find:
# 1. Students who passed BOTH subjects (intersection)
# 2. Students who passed EITHER subject (union)
# 3. Students who passed maths but NOT science (difference)
# 4. Students who passed only ONE subject not both
#    (symmetric difference)
passed_maths.union(passed_science)
print("students who passed in either subjects :",passed_maths.union(passed_science))
passed_maths.intersection(passed_science)
print("students who passed in both subjects :",passed_maths.intersection(passed_science))
for el in passed_maths:
    if (el in passed_science):
        continue 
    else:
        print("Student passed in maths but not science :",el)
        
for el in passed_maths.union(passed_science):
    if (el in passed_maths.intersection(passed_science)):
        continue
    else:
        print("Students who passed in only one subject :",el)



# ---- QUESTION 3 ----
# Remove duplicates from this list using a set
numbers = [1, 2, 3, 2, 4, 3, 5, 1,
           6, 4, 7, 5, 8, 2, 9, 1]
# Convert to set to remove duplicates
# Convert back to sorted list
new=set(numbers)
print(new)
new=list(new)
print(new)
new.sort()
print(new)


# ---- QUESTION 4 ----
# Check membership speed test
# Create a set and a list with same 10000 numbers
# Check if number 9999 exists in both
# Sets are O(1) lookup, lists are O(n)
# You won't see speed difference with small data
# but write the code and add a comment explaining
# WHY sets are faster for membership testing
large_list = list(range(10000))
large_set = set(range(10000))
# write your code here


# ========== DICTIONARIES - EASY (5-8) ==========


# ---- QUESTION 5 ----
# Create a dictionary of 5 students and their marks
# Print each student name and mark using a for loop
# Find the student with highest mark
# Find the student with lowest mark
# Add a new student
# Update an existing student's mark
# Delete one student
# Print final dictionary

dict={
    "Tushar":90,
    "ram":9,
    "hari":12,
    "std4":100,
    "std5":68,
}

highest=max(dict.values())
lowest=min(dict.values())

for el in dict:
    print(el,":",dict.get(el))


for el in dict:
    if(dict.get(el)==highest):
        print("highest  :",el,"=",highest)
    if(dict.get(el)==lowest):
        print("lowest :",el,"=",lowest)
dict.update({"syam":99})   
print(dict)

dict["Tushar"]=101
print(dict)
del dict["Tushar"]
print(dict)


# ---- QUESTION 6 ----
# Word frequency counter
sentence = "the quick brown fox jumps over the lazy dog the fox"
# Count how many times each word appears
# Store in a dictionary
# Print each word and its count
# Print the most repeated word
# Hint: split the sentence into words first
# sentence.split() gives you a list of words
# write your code here


# ---- QUESTION 7 ----
# Dictionary methods practice
student = {
    "name": "Tushar",
    "age": 20,
    "college": "KIIT",
    "branch": "AI ML",
    "cgpa": 6.31
}
# 1. Print all keys
# 2. Print all values
# 3. Print all key-value pairs using items()
# 4. Check if "cgpa" exists in dictionary
# 5. Check if "phone" exists in dictionary
# 6. Get value of "branch" using get()
#    get() is safer than direct access - explain why
#    as a comment
# 7. Update cgpa to 7.5
# 8. Add a new key "year" with value 3
# write your code here


# ---- QUESTION 8 ----
# Phone book application
# Start with empty dictionary
phonebook = {}
# 1. Add 5 contacts manually
# 2. Search for a contact by name
#    If found print number
#    If not found print "Contact not found"
# 3. Update a contact's number
# 4. Delete a contact
# 5. Print all contacts neatly
#    Name: XXXX  Number: XXXXXXXXXX
# write your code here


# ========== REAL WORLD + ADVANCED (9-13) ==========


# ---- QUESTION 9 ----
# Student grade book
students = {
    "Tushar": [85, 92, 78, 90, 88],
    "Rahul": [72, 68, 75, 80, 71],
    "Priya": [95, 98, 92, 96, 94],
    "Anita": [55, 60, 58, 62, 57],
    "Raj": [40, 45, 38, 50, 42]
}
# Each student has a list of 5 subject marks
# For each student calculate:
# 1. Total marks
# 2. Average marks
# 3. Grade (A=90+, B=75-89, C=60-74, F=below 60)
# Print a full report card for each student
# Also find class topper at the end
for el in students :
    total=0
    
    for i in students.get(el):
        total+=i    
    print( el,"Total mark:",total)
    average=total/len(students.get(el))
    print(el,"Average mark:",average)
    if (average>=90):
        print("grade A")
    elif(average>=75 and average<=89):
        print("Grade B")
    elif(average>=60 and average<=74):
        print("Grade C")
    else:
        print("Grade F")


# ---- QUESTION 10 ----
# Inventory management system
inventory = {
    "rice": {"price": 50, "quantity": 100},
    "wheat": {"price": 40, "quantity": 150},
    "sugar": {"price": 45, "quantity": 80},
    "oil": {"price": 120, "quantity": 50},
    "salt": {"price": 20, "quantity": 200}
}
# 1. Print all items with price and quantity
# 2. Calculate total inventory value
#    (price * quantity for each item)
# 3. Find items with quantity below 60
#    Print "Low stock warning" for those items
# 4. Apply 10% price increase to all items
# 5. Add a new item "dal" price 80 quantity 120
# 6. Print updated inventory

for el in inventory:
    total=1
    for i in inventory.get(el): 
        print(el,i,inventory.get(el).get(i)) 
        total*=inventory.get(el).get(i)
    print("total inventory:",total)    
                
for el in inventory:
    for i in inventory.get(el):
        if(i=="quantity"):
            if(inventory.get(el).get(i)<60):
                print("Low stock warning",el)
            else:
                continue
           
for el in inventory:
    for i in inventory.get(el):
        updated=inventory.get(el).get(i)     
        if(i=="price"):
            updated=inventory.get(el).get(i)+0.1*inventory.get(el).get(i)
        
        elif(i=="quantity"):
            continue
        print(el,i,updated)
inventory.update({"dal": {"price": 80, "quantity": 120}})
print(inventory)

# ---- QUESTION 11 ----
# Election vote counter
votes = ["Rahul", "Priya", "Rahul", "Tushar",
         "Priya", "Rahul", "Anita", "Priya",
         "Tushar", "Rahul", "Anita", "Priya",
         "Rahul", "Tushar", "Priya", "Anita"]
# 1. Count votes for each candidate
#    Store in a dictionary
# 2. Print each candidate and their vote count
# 3. Declare the winner
# 4. Print vote percentage for each candidate
#    percentage = (votes / total votes) * 100
# 5. Check if it was a majority win
#    majority = more than 50% of total votes
new={}
for el in votes:
    if (el in new):
        new[el]+=1
    else:
        new.update({el:1})
        
    
        
print(new) 

for el in new:
    if (new.get(el)==max(new.values())):
        print(el,new.get(el))
    else:
        continue
total=0
for el in new:
    total=total+new.get(el)
print(total)    
for el in new:
    print("vote percentage of ",el,(new.get(el)/total)*100)
for el in new :
    if((new.get(el)/total)*100<50):
        print(el,"not majority")
    else:
        print(el,"majority")


# ---- QUESTION 12 ----
# Railway reservation system
seats = {
    "A1": None, "A2": None, "A3": None,
    "B1": None, "B2": None, "B3": None,
    "C1": None, "C2": None, "C3": None
}
# None means seat is empty
# 1. Book seat A1 for "Tushar"
# 2. Book seat B2 for "Rahul"
# 3. Book seat A3 for "Priya"
# 4. Try to book A1 again for "Anita"
#    Print "Seat already booked" if taken
# 5. Cancel booking for B2
# 6. Print all seats - show name or "Available"
# 7. Print how many seats are booked
# 8. Print how many seats are available
for el in seats:
    if(el=="A1"):
        seats.update({"A1":"Tushar"})
    if(el=="B2"):
         seats.update({"B2":"Rahul"})
    if(el=="A3"):
         seats.update({"A3":"Priya"})
    else:
        continue
print(seats)         
    

for el in seats:
    if(el=="B2"):
        print("Booking cancelled",el,seats.update({"B2": None}))
    else:
        continue
    
for el in seats:
    if(seats.get(el) is not None):
        print("Seat already booked",el)
    else:
        print("Seat is open to book",el)
notbooked=0        
booked=0        
for el in seats:
    if(seats.get(el) is None):
        notbooked+=1
    else:
        booked+=1

print("Number of seats booked :", booked)
print("Number of seats Available :", notbooked) 


# ---- QUESTION 13 ----
# Nested dictionary - School database
school = {
    "Class10A": {
        "teacher": "Mrs. Sharma",
        "students": ["Tushar", "Rahul", "Priya"],
        "subject": "Mathematics"
    },
    "Class10B": {
        "teacher": "Mr. Verma",
        "students": ["Anita", "Raj", "Neha"],
        "subject": "Science"
    },
    "Class10C": {
        "teacher": "Mrs. Patel",
        "students": ["Vikram", "Pooja", "Arjun"],
        "subject": "English"
    }
}
# 1. Print teacher name of Class10B
# 2. Print all students of Class10A
# 3. Add a new student "Deepak" to Class10C
# 4. Add a completely new class "Class10D"
#    teacher: "Mr. Kumar"
#    students: ["Sita", "Ram", "Gita"]
#    subject: "Hindi"
# 5. Print total number of students in entire school
# 6. Find which class has "Raj" as a student

print("teacher name of Class10B :",school["Class10B"]["teacher"])
print("all students of Class10A:",school[ "Class10A"]["students"])

school["Class10C"]["students"].append("Deepak")#adds "Deepak" 
print(school)

school["Class10D"] = {
    "teacher": "Mr. Kumar",
    "students": ["Sita", "Ram", "Gita"],
    "subject": "Hindi"
}

total = 0
for el in school:
    total += len(school[el]["students"])
print("Total students:", total)

for el in school:
    if "Raj" in school[el]["students"]:
        print("Raj is in:", el)