# Problem 12: Employee Count Tracker
# Scenario: Count employee objects
# Task: Increment count when object is created

class Employee:

    # Class variable
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1


# Creating objects
e1 = Employee("Alex")
e2 = Employee("Riya")

# Printing count
print(Employee.count)