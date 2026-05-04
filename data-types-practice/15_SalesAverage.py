# Question:
# Build a list of sales amounts, compute their average, and display it rounded to two decimal points.

n = int(input("Enter number of sales: "))

sales = []

for i in range(n):
    amount = float(input("Enter sale amount: "))
    sales.append(amount)

total = sum(sales)
avg = total / n

print("Average Sales:", round(avg, 2))