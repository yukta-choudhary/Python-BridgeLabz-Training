# Problem 18: File Integrity Checker
# Scenario: Compare SHA256 hash of two files
# Task: Check if files are identical

import hashlib

def get_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

def check_integrity(file1, file2):
    if get_hash(file1) == get_hash(file2):
        print("Files are identical.")
    else:
        print("Files are different.")

# Example call
# check_integrity("file1.txt", "file2.txt")