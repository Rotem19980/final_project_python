import csv
import pandas as pd
from pip._vendor.distlib.compat import raw_input

DATA_IS_MISSING_MSG = "There's some data missing, please check your csv."
FILE_DOES_NOT_EXIST_MSG = "File does not exist."
CSV_PATH_INPUT_MSG = "Please insert the csv path: "
EMPLOYEE_INVALID_ID_MSG = 'Error! Please insert a 9 numbers employee id.'
EMPLOYEE_INVALID_AGE_MSG = "Sorry, please insert a valid age."
EMPLOYEE_INVALID_PHONE_MSG = 'Error! Please insert a valid phone number.'
EMPLOYEE_ID_INPUT_MSG = "Please add the employee's id: "
EMPLOYEE_INVALID_NAME_MSG = 'Error! Please insert a valid employee name.'
EMPLOYEE_NAME_INPUT_MSG = "Please add the employee's name: "
EMPLOYEE_AGE_INPUT_MSG = "Please add the employee's age: "
EMPLOYEE_PHONE_INPUT_MSG = "Please add the employee's phone: "

def open_and_read_file(csv_file):
    return pd.read_csv(csv_file)

def csv_data_is_supplied_test():
    """
    This function gets from the user the employees csv path as a string and checks if all data is supplied.
    employee_id = a string.
    """
    try:
        csv_path_from_user = raw_input(CSV_PATH_INPUT_MSG)
        if open_and_read_file(csv_path_from_user).isnull().values.any() == True:
            print(DATA_IS_MISSING_MSG)
    except FileNotFoundError:
        print(FILE_DOES_NOT_EXIST_MSG)

def employee_id_test():
    """
    This function gets from the user the employee's id as a string and checks if it's valid.
    employee_id = a string.
    """
    try:
        employee_id = str(input(EMPLOYEE_ID_INPUT_MSG))
        if any(char.isdigit() for char in employee_id):
            if len(str(employee_id)) == 9:
                if int(employee_id) < 100000000:
                    employee_id = str(employee_id.zfill(9))
                return str(employee_id)
            else:
                return EMPLOYEE_INVALID_ID_MSG
        else:
            return EMPLOYEE_INVALID_ID_MSG
    except ValueError:
        return EMPLOYEE_INVALID_ID_MSG

def full_name_test():
    """
    This function gets from the user a name of an employee as a string and checks if it's valid.
    name = a string.
    """
    name = str(input(EMPLOYEE_NAME_INPUT_MSG))
    while any(char.isdigit() for char in name):
        try:
            if not(any(char.isdigit() for char in name)):
                return str(name)
            else:
                return EMPLOYEE_INVALID_NAME_MSG
        except ValueError:
            return EMPLOYEE_INVALID_NAME_MSG

def phone_test():
    """
    This function gets from the user the employee's phone as a string and checks if it's valid.
    phone = a string.
    """
    try:
        phone = str(input(EMPLOYEE_PHONE_INPUT_MSG))
        if any(char.isdigit() for char in phone) == True:
            if len(str(phone)) == 10:
                if int(phone) < 100000000:
                    phone = str(phone.zfill(9))
                return str(phone)
            else:
                return EMPLOYEE_INVALID_PHONE_MSG
        else:
            return EMPLOYEE_INVALID_PHONE_MSG
    except ValueError:
        return EMPLOYEE_INVALID_PHONE_MSG

def age_test():
    """
    This function gets from the user an age of an employee as a integer and checks if it's valid.
    age = an integer.
    """
    try:
        age = int(input(EMPLOYEE_AGE_INPUT_MSG))
        if 18 < age < 100:
            return str(age)
        else:
            return EMPLOYEE_INVALID_AGE_MSG
    except ValueError:
        return EMPLOYEE_INVALID_AGE_MSG


