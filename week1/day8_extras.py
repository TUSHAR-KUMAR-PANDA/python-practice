# ==========================================
# WEEK 1 REVISION — Mixed Questions
# Topics: Variables, Conditionals, Loops,
# Lists, Tuples, Dictionaries, Sets, Functions
# Date: 27-06-2026
# ==========================================


# ---- QUESTION 1 ----
# Write a function called is_palindrome
# Takes a string as input
# Returns True if it reads same forwards and backwards
# Returns False otherwise
# Test: "racecar" → True, "hello" → False
# Do NOT use string slicing directly
# Use a loop to check character by character
# write your code here


# ---- QUESTION 2 ----
# Write a function called find_duplicates
# Takes a list of numbers
# Returns a new list containing only the duplicate numbers
# Example: [1,2,3,2,4,3,5] → [2,3]
# Do NOT use set() directly
# write your code here


# ---- QUESTION 3 ----
# You have this dictionary of monthly sales
sales = {
    "January": 45000,
    "February": 52000,
    "March": 48000,
    "April": 61000,
    "May": 55000,
    "June": 70000
}
# Write a function called analyse_sales
# that takes the sales dictionary and returns a tuple of:
# (best_month, worst_month, average_sales, total_sales)
# Then unpack and print all four values
# write your code here


# ---- QUESTION 4 ----
# Write a function called flatten_list
# Takes a list of lists
# Returns a single flat list
# Example: [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6]
# Use nested loops
nested = [[1, 2, 3], [4, 5, 6],
          [7, 8, 9], [10, 11, 12]]
# write your code here


# ---- QUESTION 5 ----
# Write a function called caesar_cipher
# Takes a message string and a shift number
# Shifts every letter by that many positions
# Example: "hello" with shift 3 → "khoor"
# Only shift letters, keep spaces and numbers as is
# Hint: use ord() to get ASCII value of character
#       use chr() to convert back to character
#       ord('a') = 97, ord('z') = 122
message = "hello tushar"
shift = 3
# write your code here


# ---- QUESTION 6 ----
# Write a function called group_by_marks
# Takes a list of student dictionaries
# Groups them into passed and failed lists
# Returns a dictionary with two keys:
# "passed" and "failed"
# Pass mark is 60
students = [
    {"name": "Tushar", "marks": 85},
    {"name": "Rahul", "marks": 45},
    {"name": "Priya", "marks": 92},
    {"name": "Anita", "marks": 58},
    {"name": "Raj", "marks": 73},
    {"name": "Neha", "marks": 38},
    {"name": "Vikram", "marks": 67}
]
# write your code here


# ---- QUESTION 7 ----
# Write a recursive function called sum_digits
# Takes a number
# Returns sum of all its digits
# Example: 1234 → 1+2+3+4 = 10
# Example: 9999 → 36
# Must use recursion
# write your code here


# ---- QUESTION 8 ----
# Write a function called common_elements
# Takes two lists
# Returns a list of elements that appear in BOTH lists
# Without using set intersection
# Use loops only
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [4, 5, 6, 7, 8, 9, 10, 11]
# write your code here


# ---- QUESTION 9 ----
# Mini inventory system using dictionary
# Write these 4 functions:
# 1. add_item(inventory, name, price, qty)
#    adds item to inventory
# 2. remove_item(inventory, name)
#    removes item, prints error if not found
# 3. update_price(inventory, name, new_price)
#    updates price, prints error if not found
# 4. show_inventory(inventory)
#    prints all items neatly with total value
#
# Test all 4 functions with sample data
inventory = {}
# write your code here


# ---- QUESTION 10 ----
# Write a function called number_to_words
# Converts numbers 1-99 to words
# 1 = "One", 15 = "Fifteen", 99 = "Ninety Nine"
# Hint: use two dictionaries
# one for 1-19 (special cases)
# one for 20,30,40...90 (tens)
# write your code here


# ---- QUESTION 11 ----
# Write a function called validate_password
# Returns a dictionary with validation results
# Checks:
# length_ok: True if length >= 8
# has_upper: True if has uppercase letter
# has_lower: True if has lowercase letter
# has_digit: True if has a number
# has_special: True if has @,#,$,%,&,*
# is_valid: True only if ALL above are True
# Print each check and final verdict
password = "Tushar@2026"
# write your code here


# ---- QUESTION 12 ----
# The ultimate function — combine everything
# Write a function called student_report_system
# Takes a list of student dictionaries
# Each student has name, marks list, attendance %
# For each student calculate:
# 1. Average marks
# 2. Grade (A/B/C/F)
# 3. Whether eligible for exam
#    (attendance must be above 75%)
# 4. Final result — Pass/Fail/Not Eligible
# Print a complete formatted report for each student
students = [
    {"name": "Tushar",
     "marks": [85, 92, 78, 90, 88],
     "attendance": 82},
    {"name": "Rahul",
     "marks": [72, 68, 75, 80, 71],
     "attendance": 70},
    {"name": "Priya",
     "marks": [95, 98, 92, 96, 94],
     "attendance": 95},
    {"name": "Anita",
     "marks": [55, 60, 58, 62, 57],
     "attendance": 78},
    {"name": "Raj",
     "marks": [40, 45, 38, 50, 42],
     "attendance": 65}
]
# write your code here