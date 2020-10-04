import csv
import datetime
import os

with open('Employees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skips the first line in the file
    for line in csv_reader:
        print(line)
x = datetime.datetime.now()


while True:
    try:
        id_input = int(input("Please enter an employee's id: "))
    except ValueError:
        print("Please insert a valid id")
        continue
    elif id_input.len() != 9:
        except ValueError:
            print("Please insert a valid id")
            continue
    else:
        break
with open('Attendance_log.csv', 'r') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        employee_id = row[0]
        if employee_id == id_input:
            print(row)



