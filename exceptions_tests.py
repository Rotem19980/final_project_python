import pandas as pd

DATA_IS_MISSING_MSG = "There's some data missing, please check your csv."
FILE_DOES_NOT_EXIST_MSG = "File does not exist."
EMPLOYEE_INVALID_ID_MSG = 'Error! Please insert a 9 numbers employee id.'
EMPLOYEE_INVALID_AGE_MSG = "Sorry, please insert a valid age."
EMPLOYEE_INVALID_PHONE_MSG = 'Error! Please insert a valid phone number.'
EMPLOYEE_INVALID_NAME_MSG = 'Error! Please insert a valid employee name.'

def read_file(csv_file):
    """
    This function gets the employees csv path as a string, opens and reads it.
    """
    return pd.read_csv(csv_file)

def csv_data_is_supplied_test(csv_path_from_user):
    """
    This function gets from the user the employees csv path as a string and checks if all data is supplied.
    csv_path_from_user = a string.
    """
    try:
        if read_file(csv_path_from_user).isnull().values.any():
            print(DATA_IS_MISSING_MSG)
    except FileNotFoundError:
        print(FILE_DOES_NOT_EXIST_MSG)

def employee_id_test(employee_id):
    """
    This function gets from the user the employee's id as a string and checks if it's valid.
    employee_id = a string.
    """
    try:
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

def full_name_test(full_name):
    """
    This function gets from the user a name of an employee as a string and checks if it's valid.
    name = a string.
    """
    while any(char.isdigit() for char in full_name):
        try:
            if not(any(char.isdigit() for char in full_name)):
                return str(full_name)
            else:
                return EMPLOYEE_INVALID_NAME_MSG
        except ValueError:
            return EMPLOYEE_INVALID_NAME_MSG

def phone_test(phone):
    """
    This function gets from the user the employee's phone as a string and checks if it's valid.
    phone = a string.
    """
    try:
        if any(char.isdigit() for char in phone):
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

def age_test(age):
    """
    This function gets from the user an age of an employee as a integer and checks if it's valid.
    age = an integer.
    """
    try:
        if 18 < age < 100:
            return str(age)
        else:
            return EMPLOYEE_INVALID_AGE_MSG
    except ValueError:
        return EMPLOYEE_INVALID_AGE_MSG


