employee_file = open("21_employees.txt","r")

for line in employee_file.readlines():
    print(line)

employee_file.close()
