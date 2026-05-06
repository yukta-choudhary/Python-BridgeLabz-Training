# Problem 2: Summary File Writer
# Scenario: The analytics team requires a script to generate a daily summary file.
# Task: Create a file named summary.txt and write:
# "Report Generated" and "Status: Success"

with open("summary.txt", "w") as file:
    file.write("Report Generated\n")
    file.write("Status: Success")