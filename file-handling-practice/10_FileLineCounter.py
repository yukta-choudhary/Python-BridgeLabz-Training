# Problem 10: File Line Counter
# Scenario: Count number of lines in a file
# Task: Write function count_lines(filename)

def count_lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count += 1
    print("Total Lines:", count)

# Example call
# count_lines("notes.txt")