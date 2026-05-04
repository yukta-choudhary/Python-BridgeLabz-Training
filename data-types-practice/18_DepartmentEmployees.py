# Question:
# Build a nested dictionary representing departments and employees.
# Print all employees belonging to a specific department entered by the user.

n = int(input("Enter number of departments: "))

departments = {}

for i in range(n):
    dept = input("Enter department name: ")
    emp_names = input("Enter employee names (comma separated): ")
    
    departments[dept] = emp_names.split(",")

search_dept = input("Enter department to view employees: ")

if search_dept in departments:
    print("Employees in", search_dept, ":")
    for name in departments[search_dept]:
        print(name)
else:
    print("Department not found")