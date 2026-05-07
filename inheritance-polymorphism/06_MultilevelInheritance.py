# Problem 6: Multi-level Inheritance
# Scenario: Company hierarchy
# Task: Demonstrate multilevel inheritance

class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, age):

        # Calling parent constructor
        super().__init__(name)

        self.age = age


class Manager(Employee):

    def __init__(self, name, age, department):

        # Calling parent constructor
        super().__init__(name, age)

        self.department = department

    def display(self):

        print("Name:", self.name,
              "| Age:", self.age,
              "| Department:", self.department)


# Creating object
m = Manager("Alex", 35, "Finance")

# Calling method
m.display()