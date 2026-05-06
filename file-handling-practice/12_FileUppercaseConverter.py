# Problem 12: File Uppercase Converter
# Scenario: Convert file content to uppercase
# Task: Read input.txt and write uppercase to output.txt

with open("input.txt", "r") as file:
    content = file.read()

with open("output.txt", "w") as file:
    file.write(content.upper())