# Problem 5: File Copier
# Scenario: Create backup of config.ini
# Task: Copy content from config.ini to config_backup.ini

with open("config.ini", "r") as source:
    content = source.read()

with open("config_backup.ini", "w") as target:
    target.write(content)