# Problem 8: Multiple Inheritance Example
# Scenario: Logger and Database system
# Task: Use multiple inheritance

class Logger:

    def log(self, message):
        print("Log:", message)


class Database:

    def save(self, data):
        print("Database entry saved:", data)


class MonitoringSystem(Logger, Database):
    pass


# Creating object
sys = MonitoringSystem()

# Calling methods
sys.log("Server started")
sys.save("Server running")