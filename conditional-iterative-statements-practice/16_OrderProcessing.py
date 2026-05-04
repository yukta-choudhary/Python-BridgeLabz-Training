# Question:
# Problem 7: Order Processing Simulator
# Stop processing when "Failed" is found.

data = input("Enter order statuses (comma separated): ")
orders = data.split(",")

for order in orders:
    if order == "Failed":
        print("Processing stopped due to Failed status.")
        break
    print("Processing order:", order)