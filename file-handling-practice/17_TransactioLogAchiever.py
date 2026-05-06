# Problem 17: Transaction Log Archiver
# Scenario: Compress all .log files
# Task: Create transactions_archive.zip

import zipfile
import os

with zipfile.ZipFile("transactions_archive.zip", "w") as zipf:
    for file in os.listdir():
        if file.endswith(".log"):
            zipf.write(file)