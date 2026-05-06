with open("daily_log.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())