import csv
import datetime
import exceptions_tests
import os
from pip._vendor.distlib.compat import raw_input

EMPLOYEE_DOESNT_EXIST_MSG = "Sorry, the employee doesn't exist."
EMPLOYEE_ALREADY_EXISTS_MSG = "Sorry, the employee is already exist."
LATE_HOUR = "09:30:00"
ADD_EMPLOYEES_FROM_FILE_MSG = "Please add the full file path of the employees you wish to add: "
EMPLOYEE_ATTENDANCE_DOESNT_EXIST_MSG = "Sorry, the employee has no data in the attendance report."
EMPLOYEE_DOESNT_EXIST_IN_FILE_MSG = "Sorry, that employee does not exist in this file."

class Employee(object):

    def __init__(self, employee_id, full_name, phone, age):
        """
        This function gets the employee's id, name, phone and age from user.
        employee_id = a string.
        full_name = a string.
        phone = a string.
        age = a string.
        """
        self.employee_id = employee_id
        self.full_name = full_name
        self.phone = phone
        self.age = age


class EmployeesList(object):

    def __init__(self, list_of_employees):
        """
        This function gets employees file's path from user.
        list_of_employees = a string.
        """
        self.list_of_employees = list_of_employees

    def add_employee(self, new_employee):
        """
        This function gets the credentials of a new employee and employees file path from from user and adds it to the file.
        new_employee = new employee's credentials.
        """
        with open(self.list_of_employees, 'r+') as list_of_employees_file:
            list_of_employees_data = csv.reader(list_of_employees_file)
            for row in list_of_employees_data:
                if new_employee.employee_id in row:
                    print(EMPLOYEE_ALREADY_EXISTS_MSG)
                    return
            list_of_employees_file.write("{}, {}, {}, {}\r\n").format(str(new_employee.employee_id), new_employee.name,
                                                                      str(new_employee.phone), str(new_employee.age))

    def add_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and adds it to the employees file
        only if all the data of all employees is supplied.
        new_employees_file_path = a string.
        """
        new_employees_file_path = raw_input(ADD_EMPLOYEES_FROM_FILE_MSG)
        try:
            with open(new_employees_file_path) as infile:
                f = open(new_employees_file_path, 'r+')
                data = f.read()
                f.close()
                f = open("employees.csv", "a")
                f.write(data)
                f.close()
        except FileNotFoundError:
            return "File does not exist."



    #how to check if all data is supplied in the file

    def delete_employee(self):
        """
        This function gets from the user a name of an employee he wishes to remove, writes all the rest of the employees to a temporary
        file and then deletes the old employees file. Afterwards, it saves it as the main employees file (employees).
        employees_name = a string.
        """
        self.full_name = exceptions_tests.full_name_test()
        with open("employees_edit.csv", "w") as my_empty_csv:
            pass
        with open('employees.csv', 'r') as inp, open('employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != self.name:
                    writer.writerow(row)
                else:
                    return EMPLOYEE_DOESNT_EXIST_IN_FILE_MSG

        os.remove('employees.csv')
        os.rename('employees_edit.csv', 'employees.csv')
    # IndexError: list index out of range
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
                    if line not in data_to_erase:
                        f.write(line)
        except FileNotFoundError:
            return "File does not exist."
    # check if all data is supplied

    def mark_attendance(self, new_employee):
        """
        The function gets an employee's id as the input and saves the date and time of him in the attendance log file.
        employee_id = a 9 numbers integer.
        monthly_report_url = a string.
        """
        attendance_data = list()
        attendance_data.append(new_employee.employee_id)
        name_to_save = None
        attendance_time = datetime.datetime.now()
        attendance_time = attendance_time.strftime('%Y/%m/%d %H:%M:%S')
        attendance_time = str(attendance_time)
        attendance_data.append(attendance_time)
        with open(self.list_of_employees) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row:
                    if str(new_employee.employee_id) == str(row[0]):
                        name_to_save = row[1]
                        attendance_data.append(str(name_to_save))
            if name_to_save == None:
                print(EMPLOYEE_DOESNT_EXIST_MSG)
            log_file = r'C:\Users\rotem\PycharmProjects\final_project_python\attendance_log.csv'
        with open(log_file, 'a') as csvFile:
            log_file = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            log_file.writerow(attendance_data)

def attendance_report_of_employee():
    """
    The function gets an employee's id as the input and prints all the entries of his attendance.
    employee_id = a 9 numbers integer.
    """
    employee_id = input("please insert the employee's id:")
    employee_exists_in_attendance_log = False
    with open(r'C:\Users\rotem\PycharmProjects\final_project_python\attendance_log.csv', 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            if row:
                if employee_id in row:
                    print(row)
                    employee_exists_in_attendance_log = True
        if employee_exists_in_attendance_log is False:
            print(EMPLOYEE_ATTENDANCE_DOESNT_EXIST_MSG)

def monthly_attendance_report():
    """
    The function prints the attendance data of all employees from the last month.
    """
    this_month = datetime.datetime.now().month
    with open(r'C:\Users\rotem\PycharmProjects\final_project_python\attendance_log.csv', 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            if row and '-' in row[1]:
                month = int(row[1].split('-')[1])
                if month == this_month:
                    return row

def late_employees_report():
    """
    The function prints the attendance data of all employees who were late (came after 09:30).
    """
    with open(r'C:\Users\rotem\PycharmProjects\final_project_python\attendance_log.csv', 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            if row:
                hour = str(row[1].split(' ')[1])
                if hour > LATE_HOUR:
                    print(row)
# def main():
#
#
# if __name__ == '__main__':
#     main()