# Question:
# Problem 2: Filename Formatter
# Write a function to clean filenames by replacing spaces with underscores and converting to lowercase.

def format_filename(name):
    name = name.replace(" ", "_")
    name = name.lower()
    return name

# input
file_name = input("Enter file name: ")

print("Formatted filename:", format_filename(file_name))