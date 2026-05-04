# Question:
# Scenario: Build a script that takes a mixed-type list like ["10", 20, "30", 40]
# Task: Convert all values to integers and compute their sum.

# taking input (comma separated)
user_input = input("Enter values separated by comma: ")

data = user_input.split(",")

total = 0

for item in data:
    num = int(item)   # convert to integer
    total += num

print("Sum:", total)