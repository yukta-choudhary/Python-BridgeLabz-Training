# Problem 11: Base and Derived Class Interaction
# Scenario: Machine and Printer system
# Task: Override start() method

class Machine:

    def start(self):
        print("Machine started")


class Printer(Machine):

    def start(self):
        print("Printer started printing...")


# Creating object
p = Printer()

# Calling method
p.start()