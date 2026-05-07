# Problem 2: Vehicle Hierarchy
# Scenario: Different vehicle types
# Task: Override start() method

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def start(self):
        print("Car started")


class Bike(Vehicle):

    def start(self):
        print("Bike started")


# Creating objects
v1 = Car()
v2 = Bike()

# Calling methods
v1.start()
v2.start()