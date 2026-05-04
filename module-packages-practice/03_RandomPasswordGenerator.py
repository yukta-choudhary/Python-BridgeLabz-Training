# Question:
# Problem 3: Random Password Generator
# Generate 8-character alphanumeric password.

import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    password = ""
    
    for i in range(8):
        password += random.choice(chars)
    
    return password

print("Password:", generate_password())