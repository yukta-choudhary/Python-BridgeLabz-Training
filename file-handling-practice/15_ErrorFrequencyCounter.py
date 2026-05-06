# Problem 15: Error Frequency Counter
# Scenario: Count "ERROR" occurrences
# Task: Print total error count

def count_errors():
    count = 0
    with open("server.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    print("Total Errors:", count)

# Example call
# count_errors()