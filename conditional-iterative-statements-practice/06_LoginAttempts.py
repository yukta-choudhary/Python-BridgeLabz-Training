# Question:
# Scenario: Monitor user login attempts.
# Task: Allow up to 3 attempts and print “Account Locked” after the third failure.

correct_password = "admin123"

for i in range(3):
    pwd = input("Enter password: ")
    
    if pwd == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")