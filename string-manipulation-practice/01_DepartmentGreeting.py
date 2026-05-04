# Question:
# Problem 1: Department Greeting Script
# Write a function that generates a greeting message using the employee’s name and department.

def greet(name, dept):
    return "Welcome " + name + " to the " + dept + " department!"

# taking input
name = input("Enter employee name: ")
dept = input("Enter department: ")

# calling function
message = greet(name, dept)
print(message)