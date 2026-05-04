# Question:
# Create a data structure (dictionary of lists) for tracking monthly revenue for different branches.
# Compute the branch with the highest total revenue.

n = int(input("Enter number of branches: "))

data = {}

for i in range(n):
    branch = input("Enter branch name: ")
    revenues = input("Enter monthly revenues (comma separated): ")
    
    rev_list = list(map(int, revenues.split(",")))
    data[branch] = rev_list

max_branch = ""
max_total = 0

for b in data:
    total = sum(data[b])
    if total > max_total:
        max_total = total
        max_branch = b

print("Highest revenue branch:", max_branch)