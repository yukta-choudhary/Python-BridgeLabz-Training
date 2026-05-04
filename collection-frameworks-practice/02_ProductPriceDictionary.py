# Question:
# Problem 2: Product Price Dictionary
# Create a dictionary mapping products to prices.

names = input("Enter product names (comma separated): ").split(",")
prices = list(map(int, input("Enter prices (comma separated): ").split(",")))

product_dict = dict(zip(names, prices))

print("Product Dictionary:", product_dict)