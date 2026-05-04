# Question:
# Develop a dictionary for storing employee data (ID, name, salary) and retrieve data by ID.

n = int(input("Enter number of employees: "))

employees = {}

for i in range(n):
    emp_id = input("Enter ID: ")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    
    employees[emp_id] = {
        "name": name,
        "salary": salary
    }

search_id = input("Enter ID to search: ")

if search_id in employees:
    print("Employee Name:", employees[search_id]["name"])
    print("Salary:", employees[search_id]["salary"])
else:
    print("Employee not found")