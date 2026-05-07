# Problem 4: Secure Bank Account

class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    # Deposit method
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited successfully")

    # Withdraw method
    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    # Getter method
    def get_balance(self):
        return self.__balance


# Taking input from the user
acc_no = int(input("Enter account number: "))
balance = int(input("Enter balance: "))

acc = BankAccount(acc_no, balance)

deposit_amount = int(input("Enter deposit amount: "))
acc.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdraw amount: "))
acc.withdraw(withdraw_amount)

print(acc.get_balance())