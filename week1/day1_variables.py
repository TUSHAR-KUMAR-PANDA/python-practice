# ==========================================
# Day 1 - Variables and Data Types
# What I learned: variables, data types,
# type conversion, arithmetic
# Date: 21-06-2026
# ==========================================

# Integers
age = 20
year = 2026

# Floats
height = 5.9
pi = 3.14159

# Strings
name = "Tushar Kumar Panda"
college = "KIIT"
branch = "AI and ML"

# Booleans
is_student = True

# Printing with comma
print("Name:", name)
print("College:", college)
print("Branch:", branch)
print("Age:", age)
print("Height:", height)

# Type checking
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))

# Arithmetic
x = 15
y = 4
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor division:", x // y)
print("Modulo:", x % y)
print("Power:", x ** y)


#String Operations
#== endswith ===
print(name.endswith("Panda")) #== output: True
print(name.endswith("sh")) #== output: False

#==capitalize ===
print(name.capitalize()) # if the starting letter is small it can convert it to capital letter 

#==find====
print(name.find("K")) # this tells on which index the letter was used for the first time 

#==count====
print(name.count("t")) # this tells how many time t has been used in the string




