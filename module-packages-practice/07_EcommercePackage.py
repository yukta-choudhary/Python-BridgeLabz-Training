# Question:
# Problem 7: Modular E-Commerce Package
# Create modules for product, order, payment.

# ---- ecommerce/product.py ----
def add_product(name, price):
    print("Product", name, "added successfully.")

# ---- ecommerce/order.py ----
def create_order(name, qty):
    print("Order created for", qty, "units of", name)

# ---- main file ----
from ecommerce.product import add_product
from ecommerce.order import create_order

add_product("Laptop", 70000)
create_order("Laptop", 2)