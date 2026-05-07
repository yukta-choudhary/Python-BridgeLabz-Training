# Problem 7: Banking Interface with Abstraction

from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


class CurrentAccount(Account):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Taking input from the user
name = input("Enter account holder name: ")
balance = int(input("Enter balance: "))

s = SavingsAccount(name, balance)

deposit_amount = int(input("Enter deposit amount: "))
s.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdraw amount: "))
s.withdraw(withdraw_amount)

print(s.get_balance())