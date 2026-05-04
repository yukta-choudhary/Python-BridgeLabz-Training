# Question:
# Scenario: Given a list of salaries, print only those above 50,000.

n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    sal = int(input("Enter salary: "))
    salaries.append(sal)

print("Salaries above 50000:")

for s in salaries:
    if s > 50000:
        print(s)