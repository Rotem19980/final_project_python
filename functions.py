class Functions(object):

    def __init__(self, ):

    def add_employee(self):
        """
        This function gets the credentials of a new employee from user and adds it to the employees file.
        new_employee = a string.
        """
        print("Please add credentials of a new employee (employee_id, name, phone, age): ")
        new_employee = input()

        if int(employee_id.len()) != 9:
            raise ValueError
            print('Error! Please insert a valid employee id.')
        elif name is not str:
            raise ValueError
            print('Error! Please insert a valid name.')

        with open('employees.csv', 'a', newline='') as file:
        file.write(new_employee)

    # need to save the input as a list and then handle exceptions.

    def add_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and adds it to the employees file
        only if all the data of all employees is supplied.
        new_employees = a string.
        """
        print("Please add the file path of the employees you wish to add: ")
        new_employees_file_path = input()
        # how to refer the input in the open command?
        f = open('new_employees.csv', "r")
        data = f.read()
        f.close()
        f = open("employees.csv", "a")
        f.write(data)
        f.close()

    # need to change to user input and add tests.

    def delete_employee(self):
        """
        This function gets from the user a name of an employee he wishes to remove, writes all the rest of the employees to a temporary
        file and then deletes the old employees file. Afterwards, it saves it as the main employees file (employees).
        employees_name = a string.
        """
        with open("employees_edit.csv", "w") as my_empty_csv:
            pass
        print("Please add the name of the employee you wish to remove: ")
        employee_name = input()
        with open('employees.csv', 'r') as inp, open('employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != employee_name:
                    writer.writerow(row)

        os.remove('employees.csv')
        os.rename('employees_edit.csv', 'employees.csv')

    # Throws back - IndexError: list index out of range, handle exceptions

    def delete_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and removes the employees from the employees file
        only if all the data of all employees is supplied.
        employees_to_delete = a string.
         """
        f = open('employees_to_delete.csv', "r")
        data = f.read()
        f.close()
        with open('employees.csv', 'r') as inp, open('employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != 'employees_to_delete.csv':
                    writer.writerow(row)
        f = open("employees.csv", "a")
        f.write(data)
        f.close()

    # Same error from above, I also want to delete it and use a one function for both deleting requests

    def mark_attendance(self):
        """
        The function gets an employee's id as the input and saves the date and time of him in the attendance log file.
        employee_id = a 9 numbers integer.
        """
        print("Please enter your id: ")
        employee_id = input()
        csvdata = [employee_id, datetime.datetime.now()]
        with open("attendance_log.csv", "a") as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            Fileout.writerow(csvdata)


        print("Please enter your id: ")
        employee_id = input()
        csvdata = [employee_id, datetime.datetime.now(), employee_name]
        with open('employees.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                name = row[1]
                if employee_id == row[0]:
                    employee_name == name
        with open("attendance_log.csv", "a") as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            Fileout.writerow(csvdata)

    # how to handle exceptions and writing every entry in a new row

    def attendance_report_of_employee(self):
        """
        The function gets an employee's id as the input and prints all the entries of his attendance.
        employee_id = a 9 numbers integer.
        """
        print("Please enter an employee's id: ")
        id_input = input()
        with open('attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                employee_id = row[0]
                if employee_id == id_input:
                    print(row)

    # To handle exceptions in input

    def monthly_attendance_report(self):
        """
        The function prints the attendance data of all employees from the last month.
        """
        this_month = datetime.datetime.now().month
        with open('attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                month = int(row[1].split('-')[1])
                if month == this_month:
                    print(row)
    # Done

    def late_employees_report(self):
        """
        The function prints the attendance data of all employees who were late (came after 09:30).
        """
        with open('attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                hour = str(row[1].split(' ')[1])
                if hour > "09:30:00":
                    print(row)
    # Done