# Question:
# Problem 6: Conditional Logger
# Print message only if debug is True.

def log_message(msg, debug=False):
    if debug:
        print(msg)

# input
msg = input("Enter message: ")
flag = input("Enable debug? (yes/no): ")

if flag == "yes":
    log_message(msg, True)
else:
    log_message(msg)