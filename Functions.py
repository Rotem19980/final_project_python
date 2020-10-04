class Functions(object):

    def __init__(self, ):

    def add_employee(self):
        print("Please add credentials of a new employee (employee_id, name, phone, age): ")
        new_employee = input()

        if int(employee_id.len()) != 9:
            raise ValueError
            print('Error! Please insert a valid employee id.')
        elif name is not str:
            raise ValueError
            print('Error! Please insert a valid name.')

        with open('Employees.csv', 'a', newline='') as file:
        file.write(new_employee)

    def add_employees_from_file(self):
        f = open('New_employees.csv', "r")
        data = f.read()
        f.close()
        f = open("Employees.csv", "a")
        f.write(data)
        f.close()

    def delete_employee(self):
        with open("Employees_edit.csv", "w") as my_empty_csv:
            pass
        print("Please add the name of the employee you wish to remove: ")
        employee_name = input()
        with open('Employees.csv', 'r') as inp, open('Employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != employee_name:
                    writer.writerow(row)

        os.remove('Employees.csv')
        os.rename('Employees_edit.csv', 'Employees.csv')

# Throws back - IndexError: list index out of range

    def delete_employees_from_file(self):
        f = open('Employees_to_delete.csv', "r")
        data = f.read()
        f.close()
        with open('Employees.csv', 'r') as inp, open('Employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != 'Employees_to_delete.csv':
                    writer.writerow(row)
        f = open("Employees.csv", "a")
        f.write(data)
        f.close()

# Same error from above, I also want to delete it and use a one function for both deleting requests

    def mark_attendance(self):
        print("Please enter your id: ")
        employee_id = input()
        csvdata = [employee_id, datetime.datetime.now()]
        with open("Attendance_log.csv", "a") as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            Fileout.writerow(csvdata)
        print("Please enter your id: ")
        employee_id = input()
        csvdata = [employee_id, datetime.datetime.now(), employee_name]
        with open('Employees.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                name = row[1]
                if employee_id == row[0]:
                    employee_name == name
        with open("Attendance_log.csv", "a") as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            Fileout.writerow(csvdata)
# איך להתמודד עם שגיאות ועם להזין נוכחות על יותר מעובד אחד

    def attendance_report_of_employee(self):
        print("Please enter an employee's id: ")
        id_input = input()
        with open('Attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                employee_id = row[0]
                if employee_id == id_input:
                    print(row)
# To handle exceptions in input
    def monthly_attendance_report(self):
        this_month = datetime.datetime.now().month
        with open('Attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                month = int(row[1].split('-')[1])
                if month == this_month:
                    print(row)
# Done
    def late_employees_report(self):
        with open('Attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                hour = str(row[1].split(' ')[1])
                if hour > "09:30:00":
                    print(row)
# Done