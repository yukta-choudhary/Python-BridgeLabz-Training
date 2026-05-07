# Problem 2: Constructor Initialization
# Scenario: Store employee ID and name
# Task: Initialize attributes using constructor

class Employee:

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name


# Creating object
emp = Employee(101, "Riya")

# Printing values
print(emp.emp_id, emp.name)