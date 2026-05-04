# Question:
# Problem 8: Age Validator and Counter
# Count how many customers are above 18.

data = input("Enter ages (comma separated): ")
ages = list(map(int, data.split(",")))

count = 0

for age in ages:
    if age > 18:
        count += 1

print("Number of customers above 18:", count)