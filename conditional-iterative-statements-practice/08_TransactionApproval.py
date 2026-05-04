# Question:
# Scenario: Simulate a transaction approval system.
# Task: If amount > 10000 → Manager Approval Required, else Approved.

n = int(input("Enter number of transactions: "))

for i in range(n):
    amount = float(input("Enter transaction amount: "))
    
    if amount > 10000:
        print("Manager Approval Required")
    else:
        print("Approved")