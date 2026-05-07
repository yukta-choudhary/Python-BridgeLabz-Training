# Problem 7: Banking Account Class
# Scenario: Simple bank account system
# Task: Deposit and withdraw money safely

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount

        else:
            print("Insufficient Balance")


# Creating object
acc = BankAccount("Alex", 1000)

# Performing operations
acc.deposit(500)
acc.withdraw(300)

# Printing balance
print(acc.balance)