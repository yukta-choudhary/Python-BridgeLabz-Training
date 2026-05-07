# Problem 14: Online Store Product Catalog
# Scenario: Manage product stock
# Task: Add and sell stock

class Product:

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):

        if quantity <= self.stock:
            self.stock -= quantity

        else:
            print("Not enough stock")


# Creating object
p = Product("Laptop", 5)

# Selling product
p.sell(2)

# Printing remaining stock
print(p.stock)