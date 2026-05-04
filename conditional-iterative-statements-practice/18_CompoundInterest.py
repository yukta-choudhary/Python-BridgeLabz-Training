# Question:
# Problem 9: Compound Interest Calculator
# Calculate compound interest using while loop.

principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
years = int(input("Enter number of years: "))

year = 1

while year <= years:
    principal = principal * (1 + rate/100)
    print("Year", year, ":", round(principal, 2))
    year += 1