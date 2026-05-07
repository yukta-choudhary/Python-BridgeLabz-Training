# Problem 4: Student Report System
# Scenario: Student performance tracker
# Task: Print Pass if marks >= 50 else Fail

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 50:
            print("Pass")

        else:
            print("Fail")


# Creating object
student = Student("Alex", 75)

# Calling method
student.grade()