# Problem 16: JSON Data Merger
# Scenario: Merge multiple JSON files
# Task: Create merged_users.json

import os
import json

data_list = []

for file in os.listdir():
    if file.endswith(".json") and file != "merged_users.json":
        with open(file, "r") as f:
            data = json.load(f)
            data_list.append(data)

with open("merged_users.json", "w") as out:
    json.dump(data_list, out)