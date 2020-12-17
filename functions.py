import csv
import datetime
import exceptions_tests
import os
from pip._vendor.distlib.compat import raw_input


class Employee(object):

    def __init__(self, employee_id, name, phone, age):
        """
        This function gets the employee's id, name, phone and age from user.
        employee_id = a string.
        name = a string.
        phone = a string.
        age = a string.
        """
        self.employee_id = employee_id
        self.name = name
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
        new_employee_data = [new_employee.employee_id, new_employee.name, new_employee.phone, new_employee.age]
        with open(self.list_of_employees, 'r+') as file1:
            existing_lines = csv.reader(file1)
            for row in existing_lines:
                if new_employee_data in row:
                    print("Sorry, the employee is already exist.")
                    return
            file1.write(str(new_employee_data) + '\n')

    def add_employees_from_file(self):
        """
        This function gets from the user a file path that contains the data of the employees and adds it to the employees file
        only if all the data of all employees is supplied.
        new_employees_file_path = a string.
        """
        new_employees_file_path = raw_input("Please add the full file path of the employees you wish to add: ")
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
        self.name = exceptions_tests.name()
        with open("employees_edit.csv", "w") as my_empty_csv:
            pass
        with open('employees.csv', 'r') as inp, open('employees_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[1] != self.name:
                    writer.writerow(row)
                else:
                    return "Sorry, that employee does not exist in this file."

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
                    if line in data_to_erase:
                        pass
                    else:
                        f.write(line)
        except FileNotFoundError:
            return "File does not exist."
    # check if all data is supplied

    def mark_attendance(self):
        """
        The function gets an employee's id as the input and saves the date and time of him in the attendance log file.
        employee_id = a 9 numbers integer.
        monthly_report_url = a string.
        """
        monthly_report_url = input("Please enter monthly attendance url: ")
        self.employee_id = exceptions_tests.employee_id_test()
        csv_data = list()
        csv_data.append(self.employee_id)
        csv_data.append(datetime.datetime.now())
        with open(self.list_of_employees) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                name = row[1]
                if self.employee_id == row[0]:
                    csv_data.append(name)
        with open(monthly_report_url, "a") as csvFile:
            fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            fileout.writerow(csv_data)

    # Done

    def attendance_report_of_employee(self):
        """
        The function gets an employee's id as the input and prints all the entries of his attendance.
        id_input = a 9 numbers integer.
        monthly_report_url = a string.
        """
        monthly_report_url = input("Please enter monthly attendance url: ")
        self.employee_id = exceptions_tests.employee_id_test()
        with open(monthly_report_url, 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                if row[0] == self.employee_id:
                    return row

    # to do

def monthly_attendance_report():
    """
    The function prints the attendance data of all employees from the last month.
    monthly_report_url = a string.
    """
    monthly_report_url = input("Please enter monthly attendance url: ")
    this_month = datetime.datetime.now().month
    with open(monthly_report_url, 'r') as csvfile:
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
                if hour > "09:30:00":
                    print(row)


# def main():
#
#
# if __name__ == '__main__':
#     main()