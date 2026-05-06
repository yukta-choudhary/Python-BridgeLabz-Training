# write in csv file
import csv

with open("sales.csv","w",newline="") as file:
    writer=csv.writer(file)

    # Writing header
    writer.writerow(["Name","Product","Price"])

    # Writing multiple rows
    writer.writerows([
            ["Alex","Laptop",50000],
            ["Sam","Phone",20000]
        ])