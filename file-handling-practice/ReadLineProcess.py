with open("logs.txt", "w") as file:
    file.write("Log1\nLog2\nLog3\n")# Create a new file and write
    file.write("Log4\n")

with open("logs.txt", "r") as file:
    for line in file:
        print(line.strip()) # Removes newline character

        #Output with strip method
        # Log1
        # Log2
        # Log3
        # Log4


        #print(line)
        #Output without strip() method
        #Log1
        #
        #Log2
        #
        #Log3
        #
        #Log4