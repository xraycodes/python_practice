# Employee booklist containing personal and miscellenous job information


#dictionary containing name, job info

employee_names = []
employee_information = {}


def employee_list_check(list):
    """
    Iterates over employee_names list and prints out. If empty list prints empty
    param: list 
    """
    if list:
        print("Current selection of employee directory contains: ")
        for index, employee in enumerate(employee_names):
            print(f"#{index + 1} {employee}")
            choice = input("Would you like to add more? y or n ")
            if choice == 'y':
                user_input = input("Add an employee to add: ")
                employee_names.append(user_input)
            if choice == 'n':
                print("The directory consists of")
                for index, names in enumerate(employee_names):
                    print(index + 1, names)
            
            
    if not list:
        print("The directory is empty")
        user_input = input("Add an employee to add: ")
        employee_names.append(user_input)
        employee_index = employee_names.index(user_input)
        employee_information.setdefault(employee_index + 1, user_input)       

# def register_name(name):
#     """
#     Appends the argument `name` to the employee_names list
#     param: name which are values received from employee_list_check() function 
#     """
#     employee_names.append(name)
    

# def employee_information():
#     employee_information = {user_input: 
#         1,
#         2,
#         3,
#     }

#main code
#while len != True:   -> why doesnt this work?
while len(employee_names) == 0:
    employee_list_check(employee_names)

employee_list_check(employee_names)


# while True:
#     print(employee_information)
#     print(employee_information[1])
#     choice = input("'a' to add info, 'b' to inquire info, 'q' to quit ")
#     if choice == 'a':
#         employee_numb = input("Which employee would you want to add information? number ")
#         print(employee_information[employee_numb]) 

#     elif choice == 'b':
#         pass
#     elif choice == 'q':
#         break
#     else:
#         print("Please enter valid choice")






   


   


#asking who the user wants to search


# for value in employee_list:
#     print(value)