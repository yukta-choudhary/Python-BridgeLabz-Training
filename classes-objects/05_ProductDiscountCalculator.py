# Problem 5: Product Discount Calculator
# Scenario: Apply discount on product price
# Task: Reduce price using percentage

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):

        self.price -= self.price * (percent / 100)


# Creating object
p = Product("Laptop", 70000)

# Applying discount
p.apply_discount(10)

# Printing updated price
print(p.price)