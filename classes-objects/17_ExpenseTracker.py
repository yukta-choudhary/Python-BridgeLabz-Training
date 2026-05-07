# Problem 17: Expense Tracker
# Scenario: Track expenses
# Task: Store transactions and calculate total expense

class ExpenseTracker:

    def __init__(self):
        self.transactions = []

    def add_expense(self, amount):
        self.transactions.append(amount)

    def total_expense(self):
        return sum(self.transactions)


# Creating object
e = ExpenseTracker()

# Adding expenses
e.add_expense(200)
e.add_expense(300)

# Printing total expense
print(e.total_expense())