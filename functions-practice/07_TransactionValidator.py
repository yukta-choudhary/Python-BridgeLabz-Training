# Question:
# Problem 7: Transaction Validator
# Return only valid transactions (amount > 0 and status == Approved)

n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    tid = int(input("Enter id: "))
    amount = int(input("Enter amount: "))
    status = input("Enter status: ")
    
    transactions.append({"id": tid, "amount": amount, "status": status})

def validate_transactions(data):
    return [t for t in data if t["amount"] > 0 and t["status"] == "Approved"]

print("Valid Transactions:", validate_transactions(transactions))