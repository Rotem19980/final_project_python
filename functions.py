import csv
import datetime
import exceptions_tests
import os
import pandas
import pandas as pd
from pip._vendor.distlib.compat import raw_input

EMPLOYEE_DOESNT_EXIST_MSG = "Sorry, the employee doesn't exist."
EMPLOYEE_ALREADY_EXISTS_MSG = "Sorry, the employee is already exist."
FILE_DOES_NOT_EXIST_MSG = "File does not exist."
LATE_HOUR = "09:30:00"
ADD_EMPLOYEES_FROM_FILE_MSG = "Please add the full file path of the employees you wish to add: "
EMPLOYEE_ATTENDANCE_DOESNT_EXIST_MSG = "Sorry, the employee has no data in the attendance report."
EMPLOYEE_DOESNT_EXIST_IN_FILE_MSG = "Sorry, that employee does not exist in this file."
EMPLOYEES_EDIT_FILE = r'C:\Users\rotem\PycharmProjects\final_project_python\employees_edit.csv'
REMOVE_EMPLOYEES_FROM_FILE_MSG = "Please add the file path of the employees you wish to remove: "
ATTENDANCE_LOG_FILE_PATH = r'C:\Users\rotem\PycharmProjects\final_project_python\attendance_log.csv'

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

    def open_and_read_file(self, list_of_employees):
        """
        This function gets employees file's path from user and returns its content.
        list_of_employees = a string.
        """
        employees_csv_data = pd.read_csv(list_of_employees)
        return employees_csv_data

    def open_and_write_employee_file(self, new_employee):
        """
        This function appends the new employee's data to the main employees file.
        new_employee = a string.
        """
        with open(self.list_of_employees, 'a', newline='') as csv_file:
            csv_file.write("\n{},{},{},{}".format(str(new_employee.employee_id), new_employee.full_name,
                                                  str(new_employee.phone), str(new_employee.age)))

    def add_employee(self, new_employee):
        """
        This function gets the credentials of a new employee and employees file path from from user and adds it to
        the file. new_employee = new employee's credentials.
        """
        employees_csv_data = self.open_and_read_file()
        for row in employees_csv_data.values:
            if new_employee.employee_id == str(row[0]):
                print(EMPLOYEE_ALREADY_EXISTS_MSG)
                return
        self.open_and_write_employee_file(new_employee)

    def add_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and adds it to the
        employees file only if all the data of all employees is supplied. new_employees_file_path = a string.
        """
        try:
            new_employees_file_path = raw_input(ADD_EMPLOYEES_FROM_FILE_MSG)
            new_employees_file_data = self.open_and_read_file(new_employees_file_path)
            employees_csv_data = self.open_and_read_file(self.list_of_employees)
            updated_csv = pandas.concat([employees_csv_data, new_employees_file_data]).drop_duplicates().reset_index(drop=True)
            updated_csv.to_csv(self.list_of_employees, index=False)
        except FileNotFoundError:
            print(FILE_DOES_NOT_EXIST_MSG)

    def delete_employee(self, new_employee):
        """
        This function gets from the user a name of an employee he wishes to remove, writes all the rest of the
        employees to a temporary file and then deletes the old employees file. Afterwards, it saves it as the main
        employees file (employees). employees_name = a string.
        """
        employees_csv_data = self.open_and_read_file(self.list_of_employees)
        with open(EMPLOYEES_EDIT_FILE, 'w') as updated_csv:
            writer = csv.writer(updated_csv)
            if str(new_employee.employee_id) not in str(employees_csv_data.values):
                print(EMPLOYEE_DOESNT_EXIST_IN_FILE_MSG)
            else:
                for row in employees_csv_data.values:
                    if new_employee.employee_id != str(row[0]):
                        writer.writerow(row)
        os.remove(self.list_of_employees)
        os.rename(EMPLOYEES_EDIT_FILE, self.list_of_employees)

    def delete_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and removes the
        employees from the employees file only if all the data of all employees is supplied. employees_to_delete = a
        string.
        """
        try:
            employees_to_delete_file_path = raw_input(REMOVE_EMPLOYEES_FROM_FILE_MSG)
            data_to_erase = self.open_and_read_file(employees_to_delete_file_path).values.tolist()
            data_to_keep = self.open_and_read_file(self.list_of_employees).values.tolist()
            with open(EMPLOYEES_EDIT_FILE, 'w') as updated_csv:
                writer = csv.writer(updated_csv)
                for row_data_to_erase in data_to_erase:
                    for row in data_to_keep:
                        if row[0] != row_data_to_erase[0] :
                            writer.writerow(row)

            os.remove(self.list_of_employees)
            os.rename(EMPLOYEES_EDIT_FILE, self.list_of_employees)
        except FileNotFoundError:
            print(FILE_DOES_NOT_EXIST_MSG)

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
            if name_to_save is None:
                print(EMPLOYEE_DOESNT_EXIST_MSG)
            log_file = ATTENDANCE_LOG_FILE_PATH
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
    with open(ATTENDANCE_LOG_FILE_PATH, 'r') as csvfile:
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
    with open(ATTENDANCE_LOG_FILE_PATH, 'r') as csvfile:
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
    with open(ATTENDANCE_LOG_FILE_PATH, 'r') as csvfile:
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