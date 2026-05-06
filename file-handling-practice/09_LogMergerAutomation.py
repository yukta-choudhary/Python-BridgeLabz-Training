# Problem 9: Log Merger Automation
# Scenario: Merge all .log files into one file
# Task: Combine contents into merged.log

import os

with open("merged.log", "w") as output:
    for file_name in os.listdir():
        if file_name.endswith(".log"):
            with open(file_name, "r") as file:
                output.write(file.read())
                output.write("\n")