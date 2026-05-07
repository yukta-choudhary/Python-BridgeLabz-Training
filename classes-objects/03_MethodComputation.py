# Problem 3: Method with Computation
# Scenario: Calculate annual salary
# Task: Return yearly salary from monthly salary

class Salary:

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12


# Creating object
sal = Salary(50000)

# Printing annual salary
print(sal.annual_salary())