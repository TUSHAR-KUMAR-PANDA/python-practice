# ==========================================
# Day 9 - Inheritance Practice
# ==========================================


# ---- QUESTION 1 - Inheritance ----
# Build a Vehicle Management System
#
# PARENT CLASS: Vehicle
# Instance variables:
#   brand, model, year, speed, is_running
#   speed starts at 0
#   is_running starts at False
#
# Instance methods:
#   start() → sets is_running to True
#              print error if already running
#   stop() → sets is_running to False
#             print error if already stopped
#   accelerate(amount) → increases speed
#                        print error if not running
#   brake(amount) → decreases speed
#                   speed cannot go below 0
#   display_info() → prints all vehicle details
#
#
# CHILD CLASS 1: Car(Vehicle)
# Additional instance variables:
#   num_doors, fuel_type
#
# Additional methods:
#   honk() → prints "Beep Beep!"
#   display_info() → shows Vehicle info + car specific info
#
#
# CHILD CLASS 2: Bike(Vehicle)
# Additional instance variables:
#   has_sidecar, bike_type
#
# Additional methods:
#   wheelie() → prints "Doing a wheelie!"
#               print error if speed < 40
#   c → shows Vehicle info + bike specific info
#
#
# CHILD CLASS 3: Truck(Vehicle)
# Additional instance variables:
#   cargo_capacity, current_cargo
#   current_cargo starts at 0
#
# Additional methods:
#   load_cargo(amount) → adds to current_cargo
#                        cannot exceed cargo_capacity
#   unload_cargo(amount) → removes from current_cargo
#                          cannot go below 0
#   display_info() → shows Vehicle info + truck specific info
#
#
# CHILD CLASS 4: ElectricCar(Car)
# This inherits from Car not Vehicle directly
# Additional instance variables:
#   battery_percentage
#   battery starts at 100
#
# Additional methods:
#   charge(amount) → increases battery
#                    cannot exceed 100
#   display_info() → shows Car info + electric specific info
#
#
# Test:
# c1 = Car("Toyota", "Camry", 2024, 4, "Petrol")
# b1 = Bike("Honda", "CBR", 2023, False, "Sport")
# t1 = Truck("Tata", "Prima", 2022, 5000)
# e1 = ElectricCar("Tesla", "Model3", 2024, 4, "Electric", 85)
#
# c1.start()
# c1.accelerate(60)
# c1.honk()
# c1.display_info()
#
# b1.start()
# b1.accelerate(50)
# b1.wheelie()
# b1.display_info()
#
# t1.start()
# t1.load_cargo(3000)
# t1.load_cargo(3000)
# t1.unload_cargo(1000)
# t1.display_info()
#
# e1.start()
# e1.accelerate(80)
# e1.charge(20)
# e1.display_info()
#
# print(isinstance(e1, Car))      # True
# print(isinstance(e1, Vehicle))  # True
# print(issubclass(ElectricCar, Car))      # True
# print(issubclass(ElectricCar, Vehicle))  # True


class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=0
        self.is_running=False
    def acceleration(self,amount):
        
        self.speed+=amount
        if(self.speed>0):
            print("The",self.brand,"is travelling at",self.speed,"Km/h")
        else:
            print("ERROR")
    def brake(self,amount):
        
        self.speed-=amount
        if(self.speed>0):
            
            print("The",self.brand,"is travelling at",self.speed,"Km/h")
        else:
            print("ERROR")
        
    def display_info(self):
        print("The",self.brand,"of model",self.model,self.year,"is traveling at a speed of",self.speed,"Km/h")
        
    def vehicle_working(self):
        if(self.speed>0):
            self.is_running=True
            print( self.is_running)
        else:
            self.is_running=False
            print( self.is_running)
            
class Car(Vehicle):
    def __init__(self,brand,model,year,num_doors,fuel_type):
        super().__init__(brand,model,year)
        self.num_doors=num_doors
        self.fuel_type=fuel_type
    def honk(self):
        print("Beep Beep")
    def display_info(self):
        super().display_info()
        print("It is",self.fuel_type,"and no of doors is:",self.num_doors)
        
class Bike(Vehicle):
    def __init__(self,brand,model,year,has_sidecar,bike_type):
        super().__init__(self,brand,model,year)
        self.has_sidecar=has_sidecar
        self.bike_type=bike_type
        
    def acceleration(self,amount):
        self.speed+=amount
        print("the bike is travelling at a speed of :",self.speed,"km/h")
    def  wheelie(self):
        if(self.speed<40):
            print("NOT DOING A WHEELIE")
        else:
            print("doing wheelie")
    def display_info(self):
        super().display_info()
        print("The bike is ",self.bike_type,self.has_sidecar)
        
class Truck(Vehicle):
    def __init__(self,brand,model,year,cargo_capacity, current_cargo):
        super().__init__(brand,model,year)
        self.cargo_capacity=cargo_capacity
        self.current_cargo=0
        
    def load_cargo(self,amount):
        self.current_cargo+=amount
        if(self.current_cargo <=self.cargo_capacity):
            print("Curret cargo weight:",self.current_cargo)
        else:
            print("ERROR")
            
    def unload_cargo(self,amount):
        self.current_cargo-=amount
        if(0<self.current_cargo<self.cargo_capacity):
            print("Total weight after unload : ",self.current_cargo)
        else:
            print("ERROR")
            
    def display_info(self):
        super().display_info()
        print(self.current_cargo)
        print(self.cargo_capacity)
        
class ElectricCar(Car):
    def __init__(self,brand,model,year,speed,is_running,num_doors,fuel_type,battery_percentage):
        
        super().__init__(brand,model,year,speed,is_running,num_doors,fuel_type)
        self.battery_percentage=0
    def charge(self,amount):
        self.battery_percentage+=amount
        if(0<=self.battery_percentage<=100):
            print("current battery parencetage is :",self.battery_percentage)
        else:
            print("ERROR")
    def display_info(self):
        super().display_info()
        print( self.battery_percentage)

# OOP INHERITANCE PRACTICE

#class Appliance:
    # brand
    # power_rating
    # is_on = False
    # usage_hours = 0

    # methods:
    # turn_on()
    # turn_off()
    # use(hours)
    # display_info()


#class WashingMachine(Appliance):
    # extra attribute: capacity

    # methods:
    # wash(clothes_kg)
    # display_info() (override)


#class AC(Appliance):
    # extra attribute: temperature = 24

    # methods:
    # set_temperature(temp)
    # display_info() (override)


class Appliance:
    def __init__(self,brand,power_rating):
        self.brand=brand
        self.power_rating=power_rating
        self.is_on=False
        self.usage_hours=0

    def turn_on(self):
        self.is_on=True
        print("Appliance is ON")

    def turn_off(self):
        self.is_on=False
        print("Appliance is OFF")

    def use(self,hours):
        if self.is_on:
            self.usage_hours+=hours
            print("Usage hours:",self.usage_hours)
        else:
            print("Turn ON first")

    def display_info(self):
        print("Brand:",self.brand)
        print("Power:",self.power_rating)
        print("On:",self.is_on)
        print("Usage:",self.usage_hours)


class WashingMachine(Appliance):
    def __init__(self,brand,power_rating,capacity):
        super().__init__(brand,power_rating)
        self.capacity=capacity

    def wash(self,clothes_kg):
        if clothes_kg<=self.capacity:
            print("Washing started")
        else:
            print("Overload error")

    def display_info(self):
        super().display_info()
        print("Capacity:",self.capacity)


class AC(Appliance):
    def __init__(self,brand,power_rating,temperature=24):
        super().__init__(brand,power_rating)
        self.temperature=temperature

    def set_temperature(self,temp):
        self.temperature=temp
        print("Temperature set to",self.temperature)

    def display_info(self):
        super().display_info()
        print("Temperature:",self.temperature)