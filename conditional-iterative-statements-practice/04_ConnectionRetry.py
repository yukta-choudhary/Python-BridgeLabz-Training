# Question:
# Scenario: Alex’s system logs failed attempts to access a database.
# Task: Retry the connection 3 times and stop once the connection succeeds.

success_attempt = int(input("Enter attempt number when connection succeeds (1-3): "))

for i in range(1, 4):
    print("Attempt", i)
    
    if i == success_attempt:
        print("Connection Successful")
        break
else:
    print("All attempts failed")