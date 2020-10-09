
print("Please add the employee's id: ")
employee_id = int(input())
count = 0
while employee_id > 0:
    count = count+1
    employee_id = employee_id/10
if count != 9:
    raise ValueError
    print('Error! Please insert a valid employee id.')
print("Please add the employee's name: ")
name = str(input())
if name is not str:
    raise ValueError
    print('Error! Please insert a valid name.')
print("Please add the employee's phone number: ")
phone = int(input())
print("Please add the employee's age: ")
age = int(input())

