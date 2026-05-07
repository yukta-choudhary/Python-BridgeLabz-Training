# Problem 13: Student Attendance System
# Scenario: Record student attendance
# Task: Update attendance using methods

class Student:

    def __init__(self, name):
        self.name = name
        self.attendance = "Absent"

    def mark_present(self):
        self.attendance = "Present"

    def mark_absent(self):
        self.attendance = "Absent"


# Creating object
s = Student("Alex")

# Marking present
s.mark_present()

# Printing attendance
print(s.attendance)