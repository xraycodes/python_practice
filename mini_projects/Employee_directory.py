# Employee booklist containing personal and miscellenous job information


#dictionary containing name, job info

employee_names = []
employee_information = {}


#Iterates over employee_name list and prints out. If empty prints empty
def employee_list_check(list):
    """
    Iterates over employee_names list and prints out. If empty list prints empty
    param: list 
    """
    if list:
        print("Current selection of employee directory contains: ")
        for index, employee in enumerate(employee_names):
            print(f"#{index + 1} {employee}")
            
            
        
    if not list:
        print("The directory is empty")
        user_input = input("Add an employee to add: ")
        employee_names.append(user_input)
#         register_name(user_input)
        

# def register_name(name):
#     """
#     Appends the argument `name` to the employee_names list
#     param: name which are values received from employee_list_check() function 
#     """
#     employee_names.append(name)
    

# def employee_information():
#     employee_information = {
#         1,
#         2,
#         3,
#     }

#main code
while len(employee_names) == 0:
    employee_list_check(employee_names)
    print(employee_names)
   


   


#asking who the user wants to search


# for value in employee_list:
#     print(value)