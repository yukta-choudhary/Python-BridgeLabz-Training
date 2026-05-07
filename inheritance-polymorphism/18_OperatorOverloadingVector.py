# Problem 18: Operator Overloading for Vector Class
# Scenario: Add and compare vectors
# Task: Overload + and == operators

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y


# Creating objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Adding vectors
v3 = v1 + v2

# Printing result
print(v3.x, v3.y, v1 == v2)