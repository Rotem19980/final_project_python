class Functions:

    def __init__(self, employee_id, name, phone, age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age

    def add_employee(self):
        """
        This function gets the credentials of a new employee from user and adds it to the employees file.
        """
        print("Please add credentials of a new employee (employee_id, name, phone, age): ")
        new_employee = input()


        with open('employees.csv', 'a', newline='') as file:
            file.write(new_employee)

    # need to save the input as a list and then handle exceptions.

    def add_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and adds it to the employees file
        only if all the data of all employees is supplied.
        new_employees = a string.
        """
        new_employees_file_path = raw_input("Please add the file path of the employees you wish to add: ")
        try:
            with open(new_employees_file_path) as infile:
                f = open(new_employees_file_path, 'r+')
                data = f.read()
                f.close()
                f = open("employees.csv", "a")
                f.write(data)
                f.close()
        except FileNotFoundError:
            print("File does not exist.")

    #how to check if all data is supplied in the file

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

    # handle exception if employee does not exist

    def delete_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and removes the employees from the employees file
        only if all the data of all employees is supplied.
        employees_to_delete = a string.
         """
        employees_to_delete_file_path = raw_input("Please add the file path of the employees you wish to add: ")
        try:
            with open(employees_to_delete_file_path, "r") as f:
                data_to_erase = f.readlines()  # read data line by line
            with open("employees.csv", "r") as f:
                data_to_keep = f.readlines()  # read data line by line

                # open file in write mode
            with open("employees.csv", "w") as f:
                for line in data_to_keep:
                    if line in data_to_erase:
                        pass
                    else:
                        f.write(line)
        except FileNotFoundError:
            print("File does not exist.")
    # check if all data is supplied

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
    # To handle exceptions in input of id
    def attendance_report_of_employee(self):
        """
        The function gets an employee's id as the input and prints all the entries of his attendance.
        id_input = a 9 numbers integer.
        """
        print("Please enter an employee's id: ")
        employee_id = input()
        with open('attendance_log.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                if row[0] == employee_id:
                    print(row)

    # To handle exceptions in input of id

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