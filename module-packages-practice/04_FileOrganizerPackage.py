# Question:
# Problem 4: Directory Organizer Package
# Move files into folders based on extension.

import os
import shutil

def organize_files(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        
        if os.path.isfile(full_path):
            ext = file.split(".")[-1]
            folder = os.path.join(path, ext)
            
            if not os.path.exists(folder):
                os.mkdir(folder)
            
            shutil.move(full_path, os.path.join(folder, file))
    
    print("Files organized successfully")

# input
path = input("Enter folder path: ")
organize_files(path)
