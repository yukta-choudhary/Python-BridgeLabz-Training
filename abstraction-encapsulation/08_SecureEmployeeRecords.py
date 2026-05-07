# Problem 8: Secure Employee Records

class EmployeeRecord:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Setter method with validation
    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Invalid salary amount")

    # Getter method
    def get_salary(self):
        return self.__salary


# Taking input from the user
name = input("Enter employee name: ")
salary = int(input("Enter salary: "))

emp = EmployeeRecord(name, salary)

new_salary = int(input("Enter new salary: "))

try:
    emp.set_salary(new_salary)
    print(emp.get_salary())

except ValueError as e:
    print(e)