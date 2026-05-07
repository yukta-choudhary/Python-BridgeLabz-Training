# Problem 7: Shape Area Calculator
# Scenario: Calculate areas of shapes
# Task: Override area() method

import math

class Shape:

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius * self.radius, 2)


# Creating objects
r = Rectangle(10, 5)
c = Circle(7)

# Printing areas
print(r.area(), c.area())