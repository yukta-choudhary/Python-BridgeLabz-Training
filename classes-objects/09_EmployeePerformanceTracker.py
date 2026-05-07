# Problem 9: Employee Performance Tracker
# Scenario: Rate employees based on projects completed
# Task: Return performance level

class Employee:

    def __init__(self, name, projects_completed):
        self.name = name
        self.projects_completed = projects_completed

    def performance(self):

        if self.projects_completed >= 10:
            return "Excellent"

        elif self.projects_completed >= 5:
            return "Good"

        else:
            return "Needs Improvement"


# Creating object
emp = Employee("Riya", 12)

# Printing performance
print(emp.performance())