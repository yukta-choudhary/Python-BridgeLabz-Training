# Question:
# Problem 3: Discount Price Calculator
# Calculate final price after discount.

def discount_price(price, discount):
    return price - (price * discount / 100)

# input
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

print("Final Price:", discount_price(price, discount))