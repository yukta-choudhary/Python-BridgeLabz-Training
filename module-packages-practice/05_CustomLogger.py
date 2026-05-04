# Question:
# Problem 5: Custom Logger Module
# Log message with timestamp.

from datetime import datetime

def log_message(level, message):
    time = datetime.now()
    print("[" + str(time) + "] " + level + ": " + message)

# input
log_message("INFO", "Server started successfully")