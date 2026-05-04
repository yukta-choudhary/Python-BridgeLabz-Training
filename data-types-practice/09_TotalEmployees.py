# Question:
# Scenario: Given a list of tuples [(“IT”, 10), (“HR”, 5), (“Finance”, 8)]
# Task: Compute the total employee count across departments.

n = int(input("Enter number of departments: "))

dept_list = []

for i in range(n):
    dept = input("Enter department name: ")
    count = int(input("Enter employee count: "))
    
    dept_list.append((dept, count))  # tuple

total = 0

for d in dept_list:
    total += d[1]

print("Total Employees:", total)