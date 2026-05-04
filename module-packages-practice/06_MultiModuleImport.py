# Question:
# Problem 6: Multi-Module Import
# Use tax.py and salary.py modules.

# ---- tax.py ----
def calculate_tax(amount):
    return amount * 0.10

# ---- salary.py ----
def calculate_net_salary(amount, tax):
    return amount - tax

# ---- main file ----
from tax import calculate_tax
from salary import calculate_net_salary

salary = 50000
tax = calculate_tax(salary)

print("Final Salary:", calculate_net_salary(salary, tax))