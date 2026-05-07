# Problem 1: Employee Inheritance Example
# Scenario: Base Employee class and Manager subclass
# Task: Display employee and department details

class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id


class Manager(Employee):

    def __init__(self, name, id, department):

        # Calling parent constructor
        super().__init__(name, id)

        self.department = department

    def display_info(self):

        print("Employee Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)


# Creating object
m = Manager("Alex", 101, "Finance")

# Calling method
m.display_info()