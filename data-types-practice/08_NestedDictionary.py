# Question:
# Scenario: Create a nested dictionary for employees with name, role, and salary.
# Task: Print all employee names earning above 50,000.

n = int(input("Enter number of employees: "))

employees = {}

for i in range(n):
    print("Enter details for employee", i+1)
    
    name = input("Name: ")
    role = input("Role: ")
    salary = int(input("Salary: "))
    
    employees[i] = {
        "name": name,
        "role": role,
        "salary": salary
    }

print("Employees earning above 50000:")

for emp in employees.values():
    if emp["salary"] > 50000:
        print(emp["name"])