# Question:
# Problem 2: Code Formatter
# Print message with 40 '-' on both sides.

def format_message(msg):
    line = "-" * 40
    print(line + msg + line)

# input
msg = input("Enter message: ")

format_message(msg)