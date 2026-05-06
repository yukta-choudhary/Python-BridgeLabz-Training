# Problem 14: Configuration Backup Script
# Scenario: Backup all .ini files
# Task: Copy from configs/ to backup/

import os
import shutil

source_folder = "configs"
backup_folder = "backup"

os.makedirs(backup_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".ini"):
        shutil.copy(source_folder + "/" + file, backup_folder)