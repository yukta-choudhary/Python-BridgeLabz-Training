# Problem 1: Basic Class Creation
# Scenario: Represent employee with name and department
# Task: Create Employee class with display_details() method

class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_details(self):
        print("Name:", self.name + ", Department:", self.department)


# Creating object
emp1 = Employee("Alex", "IT")

# Calling method
emp1.display_details()