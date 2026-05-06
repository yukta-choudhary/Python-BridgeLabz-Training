# Problem 3: Append Log Entry
# Scenario: Alex must add new log entries to an existing log file.
# Task: Append "Process Completed Successfully" to system_log.txt

with open("system_log.txt", "a") as file:
    file.write("\nProcess Completed Successfully")