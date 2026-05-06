import csv
with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    # reader is a method of csv package which creates a reader object and the reader on the left of assignment operator is  just a handle to refer to the csv file.
    for row in reader:
        print(row)