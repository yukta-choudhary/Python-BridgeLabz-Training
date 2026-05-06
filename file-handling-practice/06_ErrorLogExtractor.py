# Problem 6: Error Log Extractor
# Scenario: Extract only ERROR lines from application.log
# Task: Write those lines into error.log

with open("application.log", "r") as file:
    with open("error.log", "w") as error_file:
        for line in file:
            if "ERROR" in line:
                error_file.write(line)