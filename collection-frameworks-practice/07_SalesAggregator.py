# Question:
# Problem 7: Category-Wise Sales Aggregator
# Calculate total sales per category.

n = int(input("Enter number of entries: "))

sales = {}

for i in range(n):
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))
    
    if category in sales:
        sales[category] += amount
    else:
        sales[category] = amount

print("Total Sales:", sales)