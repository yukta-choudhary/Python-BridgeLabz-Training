# Problem 15: Multi-Level Transport Example
# Scenario: Vehicle -> Car -> ElectricCar
# Task: Demonstrate multi-level inheritance

class Vehicle:

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):

    def __init__(self, brand, model):

        # Calling parent constructor
        super().__init__(brand)

        self.model = model


class ElectricCar(Car):

    def __init__(self, brand, model, battery):

        # Calling parent constructor
        super().__init__(brand, model)

        self.battery = battery

    def display(self):

        print("Brand:", self.brand,
              "| Model:", self.model,
              "| Battery:", str(self.battery) + "%")


# Creating object
ec = ElectricCar("Tesla", "Model X", 90)

# Calling method
ec.display()