# Problem 11: File Overwriter
# Scenario: Reset log file
# Task: Overwrite process.log with "New session started"

def overwrite_file():
    with open("process.log", "w") as file:
        file.write("New session started")

# Example call
# overwrite_file()