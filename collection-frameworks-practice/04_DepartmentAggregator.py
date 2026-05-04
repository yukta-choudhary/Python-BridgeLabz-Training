# Question:
# Problem 4: Department Employee Aggregator
# Group employees by department using defaultdict.

from collections import defaultdict

n = int(input("Enter number of entries: "))

dept_dict = defaultdict(list)

for i in range(n):
    dept = input("Enter department: ")
    name = input("Enter employee name: ")
    
    dept_dict[dept].append(name)

print("Grouped Data:", dict(dept_dict))