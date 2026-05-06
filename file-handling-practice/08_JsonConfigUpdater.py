# Problem 8: JSON Config Updater
# Scenario: Update config.json
# Task: Add "debug": true and save file

import json

with open("config.json", "r") as file:
    data = json.load(file)

data["debug"] = True

with open("config.json", "w") as file:
    json.dump(data, file)                                                                                                                                                           