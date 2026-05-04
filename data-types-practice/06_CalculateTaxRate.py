# Scenario: The finance team reports that 15% tax is applied on every product.
# Task: Given cost_price and tax_rate, calculate and print selling_price.

# Taking input from user
cost_price = float(input("Enter cost price: "))
tax_rate = float(input("Enter tax rate (%): "))

# Calculating tax amount
tax_amount = (cost_price * tax_rate) / 100

# Calculating selling price
selling_price = cost_price + tax_amount

# Display result
print("Selling Price:", selling_price)