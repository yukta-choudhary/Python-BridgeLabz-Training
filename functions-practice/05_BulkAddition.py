# Question:
# Problem 5: Bulk Addition Utility
# Accept multiple numbers and return sum.

def sum_all(*numbers):
    return sum(numbers)

# input
nums = list(map(int, input("Enter numbers (comma separated): ").split(",")))

print("Sum:", sum_all(*nums))