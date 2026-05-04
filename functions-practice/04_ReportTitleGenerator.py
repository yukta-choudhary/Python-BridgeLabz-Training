# Question:
# Problem 4: Dynamic Report Title Generator
# Use default argument for department.

def format_title(title, department="Analytics"):
    return department + " Report: " + title

# input
title = input("Enter report title: ")

print(format_title(title))