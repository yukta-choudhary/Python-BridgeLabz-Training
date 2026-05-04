# Question:
# Problem 9: Employee Data Serializer
# Convert list of tuples into list of dictionaries.

n = int(input("Enter number of employees: "))

data = []

for i in range(n):
    name = input("Enter name: ")
    dept = input("Enter department: ")
    data.append((name, dept))

result = [{"name": x[0], "department": x[1]} for x in data]

print("Serialized Data:", result)