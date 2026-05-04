# Question:
# Problem 7: Recursive Directory Scanner
# List all file names in a directory.

import os

def scan_directory(path):
    files = []
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        if os.path.isdir(full_path):
            files.extend(scan_directory(full_path))
        else:
            files.append(full_path)
    
    return files

# input
path = input("Enter directory path: ")

print("Files:", scan_directory(path))