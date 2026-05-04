# Question:
# Scenario: Implement a password validation system.
# Task: Allow 3 attempts → print Access Granted or Access Denied.

correct_password = "admin123"

for i in range(3):
    pwd = input("Enter password: ")
    
    if pwd == correct_password:
        print("Access Granted")
        break
else:
    print("Access Denied")