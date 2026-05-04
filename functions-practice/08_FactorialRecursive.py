# Question:
# Problem 8: Recursive Factorial Calculator
# Calculate factorial using recursion.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# input
num = int(input("Enter number: "))

print("Factorial:", factorial(num))