# Question:
# Problem 8: Dynamic Function Router
# Execute function based on command name.

def invoke(command_name, commands_dict):
    if command_name in commands_dict:
        return commands_dict[command_name]()
    else:
        return "Invalid Command"

# commands
commands = {
    "start": lambda: "System started",
    "stop": lambda: "System stopped"
}

# input
cmd = input("Enter command: ")

print(invoke(cmd, commands))