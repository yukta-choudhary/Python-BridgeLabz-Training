# Problem 10: Vehicle Info System
# Scenario: Store vehicle details
# Task: Create Vehicle class with display() method

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand + ", Model:", self.model)


# Creating object
v = Vehicle("Tesla", "Model 3")

# Calling method
v.display()