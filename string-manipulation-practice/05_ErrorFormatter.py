# Question:
# Problem 5: Error Report Formatter
# Convert raw logs into readable format

def format_errors(text):
    lines = text.split("\n")
    
    for line in lines:
        line = line.replace("ERROR", "Error")
        line = line.replace("WARNING", "Warning")
        line = line.replace("at line", "line ")
        line = line.replace(":", " -")
        
        print(line.strip())

# input
log = input("Enter error log (use \\n for new line): ")
log = log.replace("\\n", "\n")

format_errors(log)