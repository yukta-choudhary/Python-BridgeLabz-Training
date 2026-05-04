# Question:
# Design a script that takes a product’s name, price, and discount rate, and calculates the final price.

name = input("Enter product name: ")
price = float(input("Enter price: "))
discount = float(input("Enter discount (%): "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Final price of", name, "is:", final_price)