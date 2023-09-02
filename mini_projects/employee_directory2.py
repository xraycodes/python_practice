# Employee directory featuring name, id.
# Managers have more privilage than employees


# SQLite3 for DB
import sqlite3
# con = sqlite3.connect('employee.db')
# c = con.cursor()
# c.execute("""
#         CREATE TABLE employees (
#             first_name text,
#             last_name text,
#             department text,
#             email text
#         )
#         """)
# con.commit()
# con.close()

# Datas
employee = {}

# Classes
class General:
    """Parent class that features blueprint for all employees including managers"""
    def __init__(self, first_name, last_name, department, email):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email

        employee[first_name] = (last_name, department, email)

class Manager(General):
    def check_all_employees():
        pass

class Employee(General):
    def employeefunc():
        pass


#Functions
def insert_SQL(first_name, last_name, department, email):
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("INSERT INTO employees VALUES(?, ?, ?, ?)", (first_name, last_name, department, email))
    con.commit()
    con.close()

def show_employees_db():
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("SELECT rowid, * FROM employees ")
    items = c.fetchall()
    for item in items:
        print(item)
    con.commit()
    con.close()

    
# Main code
if __name__ == '__main__':
    while True:
        print("Adding employee to the directory")
        quit = input("Press enter to continue or q to quit ")
        if quit == 'q':
            break
        employee_firstname= input("What's the first name? ")
        employee_lastname = input("What's the last name? ")
        employee_department = input("What department? ")
        employee_email = input("What's the email? ")

        insert_SQL(employee_firstname, employee_lastname, employee_department, employee_email)
        show_employees_db()

        manager_employee_question = input("Are you manager or employee? ")
        if manager_employee_question == 'manager':
            employee_firstname_class = Manager(employee_firstname, employee_lastname, employee_department, employee_email)
        if manager_employee_question == 'employee':
            employee_firstname = Employee(employee_firstname, employee_lastname, employee_department, employee_email)

        print(employee_firstname_class.first_name)
        
        