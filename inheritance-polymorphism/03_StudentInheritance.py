# Problem 3: Student Inheritance
# Scenario: General and graduate students
# Task: Add thesis title in subclass

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class GraduateStudent(Student):

    def __init__(self, name, marks, thesis):

        # Calling parent constructor
        super().__init__(name, marks)

        self.thesis = thesis

    def display(self):

        print("Student:", self.name,
              "| Marks:", self.marks,
              "| Thesis:", self.thesis)


# Creating object
g = GraduateStudent("Riya", 90, "AI in Healthcare")

# Calling method
g.display()