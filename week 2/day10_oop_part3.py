# ==========================================
# Day 10 - Dunder Methods Practice
# ==========================================

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def __str__(self):
        return f"Student: {self.name} | CGPA: {self.cgpa}"

    def __repr__(self):
        return f"Student('{self.name}', {self.cgpa})"


s1 = Student("Tushar", 6.31)

print(s1)
print(repr(s1))





# ---- QUESTION 2 - Dunder Methods ----
# Build a ShoppingCart system
# using dunder methods
#
# CLASS: ShoppingCart
# Instance variables:
#   owner, items = [], total = 0
#
# Regular methods:
#   add_item(name, price, quantity)
#   remove_item(name)
#   display_cart()
#
# Dunder methods:
#   __str__
#       returns "Cart[owner] | Items: X | Total: Rs Y"
#
#   __len__
#       returns number of items in cart
#
#   __add__
#       cart1 + cart2 combines both carts
#       returns a new cart with all items from both
#       new cart owner = "cart1owner&cart2owner"
#
#   __eq__
#       two carts are equal if their totals are same
#
#   __gt__
#       cart1 > cart2 if cart1 total is greater
#
#   __lt__
#       cart1 < cart2 if cart1 total is less
#
#   __contains__
#       "item_name" in cart
#       returns True if item exists in cart
#
#
# Test:
# cart1 = ShoppingCart("Tushar")
# cart2 = ShoppingCart("Rahul")
#
# cart1.add_item("Rice", 50, 2)
# cart1.add_item("Dal", 80, 1)
# cart1.add_item("Oil", 120, 1)
#
# cart2.add_item("Bread", 40, 2)
# cart2.add_item("Milk", 60, 3)
#
# print(cart1)
# print(len(cart1))
# print("Rice" in cart1)
# print("Bread" in cart1)
#
# combined = cart1 + cart2
# print(combined)
#
# print(cart1 == cart2)
# print(cart1 > cart2)
# print(cart1 < cart2)
#
# cart1.display_cart()
# cart1.remove_item("Dal")
# cart1.display_cart()

class ShoppingCart:

    def __init__(self, owner):
        self.owner = owner
        self.items = []   # list of dicts: {name, price, quantity}
        self.total = 0

    def add_item(self, name, price, quantity):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        self.total += price * quantity

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["price"] * item["quantity"]
                self.items.remove(item)
                print(name, "removed")
                return
        print("Item not found")

    def display_cart(self):
        print("\n--- Cart Details ---")
        for item in self.items:
            print(item["name"], item["price"], item["quantity"])
        print("Total:", self.total)

    def __str__(self):
        return f"Cart[{self.owner}] | Items: {len(self.items)} | Total: Rs {self.total}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = ShoppingCart(self.owner + "&" + other.owner)

        for item in self.items:
            new_cart.add_item(item["name"], item["price"], item["quantity"])

        for item in other.items:
            new_cart.add_item(item["name"], item["price"], item["quantity"])

        return new_cart

    def __eq__(self, other):
        return self.total == other.total

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __contains__(self, item_name):
        for item in self.items:
            if item["name"] == item_name:
                return True
        return False
    

cart1 = ShoppingCart("Tushar")
cart2 = ShoppingCart("Rahul")

cart1.add_item("Rice", 50, 2)
cart1.add_item("Dal", 80, 1)
cart1.add_item("Oil", 120, 1)

cart2.add_item("Bread", 40, 2)
cart2.add_item("Milk", 60, 3)

print(cart1)
print(len(cart1))

print("Rice" in cart1)
print("Bread" in cart1)

combined = cart1 + cart2
print(combined)

print(cart1 == cart2)
print(cart1 > cart2)
print(cart1 < cart2)

cart1.display_cart()
cart1.remove_item("Dal")
cart1.display_cart()