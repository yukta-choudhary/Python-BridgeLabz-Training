# Problem 7: CSV Sales Summary
# Scenario: Calculate total sales from sales.csv
# Task: Read CSV and print total amount

import csv

total = 0

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    
    for row in reader:
        total += int(row[1])

print("Total Sales:", total)