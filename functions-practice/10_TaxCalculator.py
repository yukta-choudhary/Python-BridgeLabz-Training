# Question:
# Problem 1: Tax Calculator
# Write a function to calculate net salary after tax deduction.

def calculate_net_salary(gross, tax_rate):
    return gross - (gross * tax_rate / 100)

# input
gross = float(input("Enter gross salary: "))
tax = float(input("Enter tax rate (%): "))

print("Net Salary:", calculate_net_salary(gross, tax))