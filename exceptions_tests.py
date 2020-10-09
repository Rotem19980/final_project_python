def employee_id_test():
    while True:
        try:
            employee_id = int(input("Please add the employee's id: "))
            if len(str(employee_id)) == 9:
                if int(employee_id) < 100000000:
                    employee_id = str(employee_id.zfill(9))
                print(employee_id)
                break
            else:
                print('Error! Please insert a 9 numbers employee id.')
        except ValueError:
            print('Error! Please insert a valid employee id.')
employee_id_test()

def age_test():
    while True:
        try:
            age = int(input("Please add the employee's age: "))
            if 18 < age < 100:
                print(age)
                break
            else:
                print("Sorry, please insert a valid age.")
        except ValueError:
            print('Error! Please insert a valid employee age.')

def name():
    while True:
        try:
            name = str(input("Please add the employee's name: "))
            if any(char.isdigit() for char in name) == False:
                print(name)
                break
            else:
                print('Error! Please insert a valid employee name.')
        except ValueError:
            print('Error! Please insert a valid employee name.')

