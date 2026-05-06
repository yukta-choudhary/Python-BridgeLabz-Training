# Problem 13: CSV Column Extractor
# Scenario: Extract "Name" column
# Task: Write names to names.txt

import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    
    with open("names.txt", "w") as out:
        for row in reader:
            out.write(row[0] + "\n")