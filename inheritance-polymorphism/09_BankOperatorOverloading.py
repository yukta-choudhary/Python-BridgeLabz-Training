# Problem 9: Operator Overloading in Bank Account
# Scenario: Add balances using + operator
# Task: Overload __add__() method

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):

        total = self.balance + other.balance

        return BankAccount(total)


# Creating objects
a1 = BankAccount(5000)
a2 = BankAccount(3000)

# Adding objects
a3 = a1 + a2

# Printing balance
print(a3.balance)