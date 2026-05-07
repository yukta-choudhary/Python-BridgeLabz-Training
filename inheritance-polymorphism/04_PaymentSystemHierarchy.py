# Problem 4: Payment System Hierarchy
# Scenario: Different payment methods
# Task: Override process_payment() method

class Payment:

    def process_payment(self):
        print("Processing payment...")


class CreditCardPayment(Payment):

    def process_payment(self):
        print("Processing credit card payment...")


class UPIPayment(Payment):

    def process_payment(self):
        print("Processing UPI payment...")


# Creating objects
p1 = CreditCardPayment()
p2 = UPIPayment()

# Calling methods
p1.process_payment()
p2.process_payment()