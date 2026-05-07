# Problem 15: Invoice Generator
# Scenario: Generate invoice for client
# Task: Return formatted invoice string

class Invoice:

    def __init__(self, client_name, amount):
        self.client_name = client_name
        self.amount = amount

    def generate_invoice(self):
        return "Invoice for " + self.client_name + " | Amount: " + str(self.amount)


# Creating object
inv = Invoice("Riya", 5000)

# Printing invoice
print(inv.generate_invoice())