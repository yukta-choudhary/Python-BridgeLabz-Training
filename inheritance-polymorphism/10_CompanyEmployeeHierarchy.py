# Problem 10: Company Employee Hierarchy
# Scenario: Employee and Manager classes
# Task: Add bonus to manager salary

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, bonus):

        # Calling parent constructor
        super().__init__(name, salary)

        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


# Creating object
m = Manager("Riya", 60000, 10000)

# Printing total salary
print(m.total_salary())