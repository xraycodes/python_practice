# Employee booklist containing personal and miscellenous job information


#dictionary containing name, job info


#asking who the user wants to search

employee_name = []
employee_information = {}
Flag = False

#Iterates over employee_name list and prints out. If empty prints empty
def employee_list_check(list):
    if list:
        print("Current selection of employee directory contains: ")
        for index, employee in enumerate(employee_name):
            print(f"#{index + 1} {employee}")
        
    if not list:
        print("The directory is empty")
        user_input = input("Add an employee to add: ")
        register_name(user_input)
        

def register_name(name):
    employee_name.append(name)
    

    
def employee_information():
    employee_information = {
        1,
        2,
        3,
    }

#main code
while Flag == True:
    employee_list_check(employee_name)
    print(employee_name)
    if employee_name:
        Flag: False

    




# for value in employee_list:
#     print(value)