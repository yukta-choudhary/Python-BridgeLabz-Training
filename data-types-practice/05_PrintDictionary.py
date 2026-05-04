#Scenario: Alex receives employee details from an API as key-value pairs.
#ask: Store them in a dictionary and print the employee’s department.

# Taking input from user
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

# Storing in dictionary
employee = {
    "name": name,
    "id": emp_id,
    "department": department,
    "salary": salary
}

# Printing the department
print("Employee Department is ", employee["department"])