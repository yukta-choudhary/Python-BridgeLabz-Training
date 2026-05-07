# Problem 1: Employee Data Protector

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Setter method
    def set_salary(self, salary):
        self.__salary = salary

    # Getter method
    def get_salary(self):
        return self.__salary


# Taking input from the user
name = input("Enter employee name: ")
salary = int(input("Enter salary: "))

emp = Employee(name, salary)

new_salary = int(input("Enter new salary: "))
emp.set_salary(new_salary)

print(emp.get_salary())