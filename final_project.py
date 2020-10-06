import csv
import datetime
import os

with open('employees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skips the first line in the file
    for line in csv_reader:
        print(line)
x = datetime.datetime.now()

