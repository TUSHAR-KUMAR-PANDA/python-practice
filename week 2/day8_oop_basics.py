# ==========================================

# OOP Practice — Bank Account System

# ==========================================

# Create a class called BankAccount.
# Build a bank account system using OOP.
# Requirements:
# 1. Every account should store:
# - Account owner
# - Current balance
# - Transaction history
# 2. Add functionality to:
# - Deposit money
# - Withdraw money
# - View account statement
# Rules:
# - Deposit amount cannot be invalid
# - Withdrawal amount cannot be invalid
# - Withdrawal greater than balance should fail
# - All successful transactions should be stored
# Create two separate bank accounts.
# Perform multiple operations on both accounts.
# Finally display complete statement
# of both accounts.
# Solve completely using classes and objects.
# After solving send your code.


class BankAccount:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
       
    def addedamount(self,amount):
        if(amount<0):
            print("the deposit amount is invalid ")
        else:
            self.balance+=amount 
            print("The new balance after deposit is ",self.balance) 
            print("The deposit amount is",amount)
    def withdrawl(self,amount):
        if(amount>self.balance):
            print("Invalid Enter valid  amount:")
        else:
            self.balance-=amount
            print("The current balance after withdrwal is:",self.balance)
            print("The withdrawn balance is ;",amount )
            

acc1=BankAccount("Tushar",10000)
acc2=BankAccount("Hari",8000)

print(acc1.withdrawl(2000))

# ==========================================
# Mini Project - Concept 1 + 2 Combined
# Hospital Management System
# ==========================================

# Build a Hospital Management System
# using ONLY what you know so far:
# classes, objects, __init__, self,
# instance variables, class variables

# Your class is called Hospital

# CLASS VARIABLES needed:
# hospital_name = "KIIT Medical Centre"
# total_patients = 0
# total_doctors = 0
# all_patients = []

# INSTANCE VARIABLES needed (in __init__):
# patient_name
# patient_id
# age
# disease
# doctor_assigned
# is_admitted = True
# bill = 0

# METHODS needed:

# 1. display_patient_info(self)
#    Print all patient details neatly like:
#    ================================
#    Patient Name : Tushar
#    Patient ID   : P001
#    Age          : 20
#    Disease      : Fever
#    Doctor       : Dr. Sharma
#    Status       : Admitted
#    Bill         : Rs 0
#    ================================

# 2. add_bill(self, amount)
#    Adds amount to patient's bill
#    Print error if amount is negative
#    Print updated bill after adding

# 3. discharge_patient(self)
#    Sets is_admitted to False
#    Prints discharge summary with final bill
#    Print error if patient already discharged

# 4. assign_doctor(self, doctor_name)
#    Updates doctor assigned to this patient
#    Print confirmation message

# 5. get_status(self)
#    Returns "Admitted" if is_admitted is True
#    Returns "Discharged" if is_admitted is False

# CLASS METHODS needed:

# 6. get_hospital_info(cls)
#    Prints hospital name and total patients

# 7. get_all_admitted_patients(cls)
#    Returns list of all patients still admitted
#    from all_patients list


# TEST YOUR SYSTEM:

# p1 = Hospital("Tushar", "P001", 20, "Fever", "Dr. Sharma")
# p2 = Hospital("Rahul", "P002", 35, "Fracture", "Dr. Verma")
# p3 = Hospital("Priya", "P003", 28, "Migraine", "Dr. Patel")
# p4 = Hospital("Anita", "P004", 45, "Diabetes", "Dr. Singh")

# p1.display_patient_info()
# p1.add_bill(500)
# p1.add_bill(1200)
# p1.discharge_patient()
# p1.discharge_patient()  # should show error

# p2.assign_doctor("Dr. Kumar")
# p2.add_bill(3000)

# Hospital.get_hospital_info()

# admitted = Hospital.get_all_admitted_patients()
# print("Currently admitted patients:")
# for p in admitted:
#     print(p.patient_name, "-", p.disease)

class Hospital:

    hospital_name = "KIIT Medical Centre"
    total_patients = 0
    total_doctors = 0
    all_patients = []

    def __init__(self, patient_name, patient_id, age, disease, doctor_assigned):
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.age = age
        self.disease = disease
        self.doctor_assigned = doctor_assigned
        self.is_admitted = True
        self.bill = 0

        Hospital.total_patients += 1
        Hospital.all_patients.append(self)

    def display_patient_info(self):
        print("Patient Name:", self.patient_name)
        print("Patient ID:", self.patient_id)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor:", self.doctor_assigned)
        print("Status:", self.get_status())
        print("Bill: Rs", self.bill)

    def add_bill(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            self.bill += amount
            print("Updated bill:", self.bill)

    def discharge_patient(self):
        if self.is_admitted == False:
            print("Patient already discharged")
        else:
            self.is_admitted = False
            print("Patient discharged")
            print("Final bill:", self.bill)

    def assign_doctor(self, doctor_name):
        self.doctor_assigned = doctor_name
        print("Doctor assigned:", self.doctor_assigned)

    def get_status(self):
        if self.is_admitted:
            return "Admitted"
        return "Discharged"

    @classmethod
    def get_hospital_info(cls):
        print("Hospital:", cls.hospital_name)
        print("Total Patients:", cls.total_patients)

    @classmethod
    def get_all_admitted_patients(cls):

        admitted = []

        for patient in cls.all_patients:
            if patient.is_admitted:
                admitted.append(patient)

        return admitted


p1 = Hospital("Tushar", "P001", 20, "Fever", "Dr. Sharma")
p2 = Hospital("Rahul", "P002", 35, "Fracture", "Dr. Verma")
p3 = Hospital("Priya", "P003", 28, "Migraine", "Dr. Patel")
p4 = Hospital("Anita", "P004", 45, "Diabetes", "Dr. Singh")


p1.display_patient_info()

p1.add_bill(500)
p1.add_bill(1200)

p1.discharge_patient()
p1.discharge_patient()

p2.assign_doctor("Dr. Kumar")
p2.add_bill(3000)

Hospital.get_hospital_info()

admitted = Hospital.get_all_admitted_patients()

for p in admitted:
    print(p.patient_name, "-", p.disease)
    
        self.is_admitted = False
        print("Patient discharged")
        print("Final bill:", self.bill)

def assign_doctor(self, doctor_name):
    self.doctor_assigned = doctor_name
    print("Doctor assigned:", self.doctor_assigned)

def get_status(self):
    if self.is_admitted:
        return "Admitted"
    return "Discharged"

@classmethod
def get_hospital_info(cls):
    print("Hospital:", cls.hospital_name)
    print("Total Patients:", cls.total_patients)

@classmethod
def get_all_admitted_patients(cls):
    admitted = []

    for patient in cls.all_patients:
        if patient.is_admitted:
            admitted.append(patient)

    return admitted


p1 = Hospital("Tushar", "P001", 20, "Fever", "Dr. Sharma")
p2 = Hospital("Rahul", "P002", 35, "Fracture", "Dr. Verma")
p3 = Hospital("Priya", "P003", 28, "Migraine", "Dr. Patel")
p4 = Hospital("Anita", "P004", 45, "Diabetes", "Dr. Singh")

p1.display_patient_info()

p1.add_bill(500)
p1.add_bill(1200)

p1.discharge_patient()
p1.discharge_patient()

p2.assign_doctor("Dr. Kumar")
p2.add_bill(3000)

Hospital.get_hospital_info()

admitted = Hospital.get_all_admitted_patients()

# ==========================================
# OOP Practice - All 3 Concepts
# ==========================================


# ---- QUESTION 1 - Instance Methods ----
# Build a class called Phone
# Instance variables: brand, model, battery, is_on
# battery starts at 100
# is_on starts at False
#
# Methods:
# turn_on()
# turn_off()
# make_call(contact)
# charge(amount)
# display_status()
#
# Test:
# p1 = Phone("Samsung", "S24")
# p2 = Phone("Apple", "iPhone 15")
# p1.turn_on()
# p1.make_call("Rahul")
# p1.make_call("Priya")
# p1.charge(50)
# p1.display_status()
# p2.make_call("Tushar")


# ---- QUESTION 2 - Class Methods ----
# Build a class called Restaurant
# Class variables: restaurant_name, total_orders,
#                  all_orders, gst
# Instance variables: item_name, price, quantity
#
# Instance method:
# display_order()
#
# Class methods:
# from_string(cls, order_string)
# get_restaurant_info(cls)
# update_gst(cls, new_gst)
# get_most_expensive_order(cls)
#
# Test:
# o1 = Restaurant("Pizza", 299, 2)
# o2 = Restaurant("Burger", 149, 3)
# o3 = Restaurant.from_string("Pasta-199-1")
# o1.display_order()
# Restaurant.get_restaurant_info()
# Restaurant.update_gst(0.08)
# expensive = Restaurant.get_most_expensive_order()
# print("Most expensive:", expensive.item_name)


# ---- QUESTION 3 - Static Methods ----
# Build a class called Validator
# No class variables
# No instance variables
# No __init__ needed
#
# Static methods:
# validate_email(email)
# validate_phone(phone)
# validate_age(age)
# validate_pin(pin)
# validate_password(password)
#
# Test:
# print(Validator.validate_email("tushar@gmail.com"))
# print(Validator.validate_email("tushargmail.com"))
# print(Validator.validate_phone("9876543210"))
# print(Validator.validate_phone("98765"))
# print(Validator.validate_age(20))
# print(Validator.validate_age(150))
# print(Validator.validate_pin("1234"))
# print(Validator.validate_pin("12345"))
# print(Validator.validate_password("Tushar2026"))
# print(Validator.validate_password("tushar"))


# ---- QUESTION 4 - Instance + Class Methods ----
# Build a class called Employee
# Class variables: company, total_employees,
#                  all_employees, min_salary
# Instance variables: name, employee_id,
#                     department, salary
#
# Instance methods:
# display_info()
# give_raise(amount)
# transfer(new_department)
# is_well_paid()
#
# Class methods:
# from_string(cls, emp_string)
# get_company_info(cls)
# get_highest_paid(cls)
# get_department_employees(cls, department)
# update_company_name(cls, new_name)
#
# Test:
# e1 = Employee("Tushar", "E001", "ML", 45000)
# e2 = Employee("Rahul", "E002", "Backend", 55000)
# e3 = Employee("Priya", "E003", "ML", 70000)
# e4 = Employee.from_string("Anita-E004-Data-60000")
# e1.display_info()
# e1.give_raise(5000)
# e1.transfer("AI Research")
# Employee.get_company_info()
# highest = Employee.get_highest_paid()
# print("Highest paid:", highest.name)
# ml_team = Employee.get_department_employees("ML")
# for emp in ml_team:
#     print(emp.name)


# ---- QUESTION 5 - Student Management System ----
# Build class called StudentManagement
#
# Class variables:
# school_name, total_students,
# passing_cgpa, all_students
#
# Instance variables:
# name, roll_number, branch,
# cgpa, attendance, subjects
#
# Instance methods:
# display_info()
# update_cgpa(new_cgpa)
# update_attendance(percentage)
# add_subject(subject)
# is_passing()
# is_eligible_for_exam()
# get_status()
#
# Class methods:
# from_string(cls, student_string)
# get_school_info(cls)
# get_topper(cls)
# get_students_below_attendance(cls, threshold)
#
# Static methods:
# validate_cgpa(cgpa)
# validate_attendance(attendance)
# get_grade(cgpa)
#
# Test:
# s1 = StudentManagement("Tushar","2201","AI ML",6.31,82.0)
# s2 = StudentManagement("Rahul","2202","CSE",7.5,70.0)
# s3 = StudentManagement("Priya","2203","ECE",8.9,91.0)
# s4 = StudentManagement("Anita","2204","ME",5.8,65.0)
# s5 = StudentManagement("Raj","2205","EEE",9.2,88.0)
# s6 = StudentManagement.from_string("Neha-2206-CSE-7.8-79.0")
# s1.display_info()
# s1.update_cgpa(7.2)
# s2.update_attendance(68.0)
# s1.add_subject("Machine Learning")
# s1.add_subject("Python")
# s1.add_subject("Python")
# print(s1.is_passing())
# print(s2.is_eligible_for_exam())
# print(s3.get_status())
# StudentManagement.get_school_info()
# topper = StudentManagement.get_topper()
# print("Topper:", topper.name)
# low = StudentManagement.get_students_below_attendance(75)
# for student in low:
#     print(student.name, student.attendance)
# print(StudentManagement.validate_cgpa(6.5))
# print(StudentManagement.validate_cgpa(11))
# print(StudentManagement.get_grade(8.5))
# print(StudentManagement.get_grade(5.9))

class StudentManagement:
    school_name="DAV PUBLIC SCHOOL"
    total_students=0
    passing_cgpa=6.5
    all_students=[]
    
    def __init__(self,name,roll_number,branch,cgpa,attendance,subjects):
        self.name=name
        self.roll_number=roll_number
        self.branch=branch
        self.cgpa=cgpa
        self.attendance=attendance
        self.subjects=subjects
        StudentManagement.total_students+=1    
        StudentManagement.all_students.append(self.name)
    def display_info(self):
        print("Name :",self.name,"Roll Number:",self.roll_number,"Branch",self.branch,"cgpa",self.cgpa,"Attendance",self.attendance,self.subjects)
    def update_cgpa(self,new_cgpa):
        self.cgpa=new_cgpa
        print("New cgpa is :",self.cgpa)
    def update_attendance(self,percentage):
        self.attendance=percentage
        print("New Attendance :",self.attendance,"%")
    def add_subject(self,subject):
        self.subjects.append(subject)
        print(self.subjects)
    def is_passing(self):
        
        if(self.cgpa>StudentManagement.passing_cgpa):
            print(self.name ,"is passing")
        else:
            print(self.name,"is not passing")
    def is_eligible_for_exam(self):
        if(self.attendance<75):
            print("Not Eligible:")
        else:
            print("Eligible")
            
    def get_status(self):
        if(self.cgpa>9.0):
            print("Excellent")
        elif(7<self.cgpa<9):
            print("great")
        else:
            print("Try Hard")
            
            
    @classmethod
    def from_string(cls, student_string):
        name,roll_number,branch,cgpa,attendance,subjects=student_string.split("-")
        return cls(name,roll_number,branch,cgpa,attendance,subjects)
    @classmethod
    def get_school_info(cls):
        print(StudentManagement.school_name)
        print(StudentManagement.total_students)
        print(StudentManagement.passing_cgpa)
        print(StudentManagement.all_students)
    @classmethod

    def get_students_below_attendance(cls, threshold):
        result = []
        for student in cls.all_students:
            if student.attendance < threshold:
                result.append(student)
        return result
    @classmethod
    def get_topper(cls):
        topper = cls.all_students[0]
        for student in cls.all_students:
            if student.cgpa > topper.cgpa:
                topper = student
        return topper
        
    def validate_cgpa(cgpa):
        if(0<cgpa<=10):
            print("VALID")
        else:
            print("INVALID")
            
    def validate_attendance(attendance):
        if(30<=attendance<=100):
            print("VALID")
        else:
            print("INVALID")
    
    def get_grade(cgpa):
        if(cgpa>=9):
            print("Grade A")
        elif(7<=cgpa<9):
            print("GRADE B")
        elif(6<=cgpa<7):
            print("GRADE C")
        else:
            print("GRADE F")
