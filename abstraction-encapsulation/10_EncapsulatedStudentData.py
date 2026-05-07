# Problem 10: Encapsulated Student Data

class Student:

    def __init__(self, name):
        self.name = name
        self.__marks = 0

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks

    # Getter method
    def get_marks(self):
        return self.__marks


# Taking input from the user
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s = Student(name)

s.set_marks(marks)

print(s.get_marks())