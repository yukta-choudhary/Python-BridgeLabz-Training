# Question:
# Problem 4: Production Target Checker
# Print days where production is below target.

data = input("Enter production units (comma separated): ")
target = int(input("Enter target: "))

units = list(map(int, data.split(",")))

for i in range(len(units)):
    if units[i] < target:
        print("Day", i+1, ":", units[i], "units (below target)")