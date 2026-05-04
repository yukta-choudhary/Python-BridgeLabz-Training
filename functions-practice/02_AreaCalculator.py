# Question:
# Problem 2: Area Calculator
# Define a function to calculate area of rectangle.

def calculate_area(length, width):
    return length * width

# input
l = int(input("Enter length: "))
w = int(input("Enter width: "))

print("Area:", calculate_area(l, w))