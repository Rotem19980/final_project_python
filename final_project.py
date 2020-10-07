import csv
import datetime
import os #this is needed for using directory paths and manipulating them
import sys

from pip._vendor.distlib.compat import raw_input

with open('employees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skips the first line in the file
    for line in csv_reader:
        print(line)
x = datetime.datetime.now()




