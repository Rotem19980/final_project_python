import pandas as pd
from pip._vendor.distlib.compat import raw_input

def csv_data_is_supplied_test():
   try:
       csv_path_from_user = raw_input("Please insert the csv path: ")
       test = pd.read_csv(csv_path_from_user)
       x = test.isnull().any(axis=1)
       missing_data_rows = x[x == True].index.to_numpy()
       if missing_data_rows.size > 0:
           print("There's some data missing, please check your csv.")
   except FileNotFoundError:
       print('File does not exist.')

def employee_id_test():
    """
    This function gets from the user the employee's id as a string and checks if it's valid.
    employee_id = a string.
    """
    while True:
        try:
            employee_id = str(input("Please add the employee's id: "))
            if any(char.isdigit() for char in employee_id) == True:
                if len(str(employee_id)) == 9:
                    if int(employee_id) < 100000000:
                        employee_id = str(employee_id.zfill(9))
                    return str(employee_id)
                else:
                    return 'Error! Please insert a 9 numbers employee id.'
            else:
                return 'Error! Please insert a 9 numbers employee id.'
        except ValueError:
            return 'Error! Please insert a valid employee id.'

def full_name_test():
    """
    This function gets from the user a name of an employee as a string and checks if it's valid.
    name = a string.
    """
    while True:
        try:
            name = str(input("Please add the employee's name: "))
            if any(char.isdigit() for char in name) == False:
                return str(name)
            else:
                return 'Error! Please insert a valid employee name.'
        except ValueError:
            return 'Error! Please insert a valid employee name.'

# to check that we get a full name

def phone_test():
    """
    This function gets from the user the employee's phone as a string and checks if it's valid.
    phone = a string.
    """
    while True:
        try:
            phone = str(input("Please add the employee's phone: "))
            if any(char.isdigit() for char in phone) == True:
                if len(str(phone)) == 10:
                    if int(phone) < 100000000:
                        phone = str(phone.zfill(9))
                    return str(phone)
                else:
                    return 'Error! Please insert a 10 digits phone number.'
            else:
                return 'Error! Please insert a 10 digits phone number.'
        except ValueError:
            return 'Error! Please insert a valid phone number.'

def age_test():
    """
    This function gets from the user an age of an employee as a integer and checks if it's valid.
    age = an integer.
    """
    while True:
        try:
            age = int(input("Please add the employee's age: "))
            if 18 < age < 100:
                return str(age)
            else:
                return "Sorry, please insert a valid age."
        except ValueError:
            return 'Error! Please insert a valid employee age.'


