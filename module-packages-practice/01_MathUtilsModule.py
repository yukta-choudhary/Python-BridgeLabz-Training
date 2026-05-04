 # Question:
# Problem 1: Simple Math Module
# Create math_utils.py with add and subtract functions and import it.

# ---- math_utils.py ----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# ---- main file ----
from math_utils import add, subtract

print(add(5, 3))
print(subtract(10, 4))