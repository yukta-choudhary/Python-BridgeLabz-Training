# Problem 18: Employee Hierarchy Manager
# Scenario: Model employee hierarchy
# Task: Create Employee base class and Manager subclass

class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department


class Manager(Employee):

    def __init__(self, name, department, team_size):

        # Calling parent constructor
        super().__init__(name, department)

        self.team_size = team_size

    def display(self):
        print("Manager:", self.name,
              "| Department:", self.department,
              "| Team Size:", self.team_size)


# Creating object
m = Manager("Alex", "IT", 10)

# Calling method
m.display()