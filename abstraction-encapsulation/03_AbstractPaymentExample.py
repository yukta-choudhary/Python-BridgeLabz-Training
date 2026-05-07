# Problem 3: Abstract Payment Example

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(Payment):

    def process_payment(self, amount):
        print("Processing card payment of", amount)


# Taking input from the user
amount = int(input("Enter payment amount: "))

p = CardPayment()
p.process_payment(amount)