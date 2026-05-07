# Problem 13: Banking System with Inheritance
# Scenario: Savings account with interest
# Task: Deposit, withdraw and add interest

class Account:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount

        else:
            print("Insufficient Balance")


class SavingsAccount(Account):

    def add_interest(self):

        # 5% interest
        self.balance += self.balance * 0.05


# Creating object
s = SavingsAccount("Alex", 10000)

# Performing operations
s.deposit(5000)
s.add_interest()

# Printing balance
print(s.balance)