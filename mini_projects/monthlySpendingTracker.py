# Program designed to keep track of monthly expenses
# Calculates Cash Flow (Money going out, in, net)

from datetime import datetime
import sqlite3

#Setting up SQLite3 DB
# con = sqlite3.connect('monthly_spending.db')
# c = con.cursor()
# table = """ CREATE TABLE tracker (
#         Month TEXT,
#         Year INT,
#         Expense_total INT,
#         Income_total INT,
#         Cash_Flow INT
#         )"""
# c.execute(table)
# print("table ready")
# con.commit()
# con.close()


# con = sqlite3.connect('monthly_spending.db')
# c = con.cursor()
# c.execute("INSERT INTO tracker VALUES ('August', 2023, 1000, 2000, 1000)")
# con.commit()
# con.close()

# con = sqlite3.connect('monthly_spending.db')
# c = con.cursor()
# c.execute("SELECT * FROM tracker")
# print(c.fetchall())


#CONSTANTS
CURRENT_MONTH = datetime.now().strftime("%B")

# Database
    # Monthly spending. Dictionary(Key: Month, Value: Spendings)
monthly_finance = {}

expenses = {}
assets = {}

#Client side
    # Option to 1) enter items for the month or 2)to look through previous months
    # Output 1: Which items to enter for that month
    # Output 2: Which previous month user requests

    # Add up total for liability
    # Add up total for asset/monthly income
    # Count for net 

#functions
def expense_tracker(month):
    while True:
        print(f"Write the expenses for {month}, type quit when finished")
        expense = input("What's the name of the expense?: ")
        if expense == 'quit':
            break
        expense_amount = int(input(f"How much did {expense} cost?: $"))
        expenses[expense] = expense_amount
        print(f"Adding {expense} with the amount ${expense_amount}")
        print(f"Expenses list for {month}: {expenses}\n")

def asset_tracker(month):
    while True:
        print(f"\nWrite the asset for {month}, type quit when finished")
        asset = input("Whats the name of the asset?: ")
        if asset == 'quit':
            break
        asset_amount = int(input(f"How much was the {asset} aquired?: $"))
        assets[asset] = asset_amount
        print(f"Adding {asset} with the amount {asset_amount}")
        print(assets)

def cash_flow():
    expense_total = 0 
    for expense_sum in expenses.values():
        expense_total += expense_sum
    
    asset_total = 0
    for asset_sum in assets.values():
        asset_total += asset_sum
    print()
    print(f"The total liability for the month of {CURRENT_MONTH} was ${expense_total}")
    print(f"The total asset for the month of {CURRENT_MONTH} was ${asset_total}")
    net = asset_total - expense_total
    print(f"The total net income for the month of {CURRENT_MONTH} was ${net}")
    monthly_finance[CURRENT_MONTH] = net

    def insert_sql(month, year, expense, income, net_income):
        con = sqlite3.connect('monthly_spending.db')
        c = con.cursor()
        c.execute("INSERT INTO tracker VALUES (?, ?, ?, ?, ?)", (month, year, expense, income, net_income))
        con.commit()
        con.close()

    insert_sql(CURRENT_MONTH, 2023, expense_total, asset_total, net )

def see_month_finance():
    con = sqlite3.connect('monthly_spending.db')
    c = con.cursor()
    c.execute("SELECT * FROM tracker")
    print(c.fetchall())


#Main Code

while True:
    user_option = input(
    """Choose option 1 to add tracker for current month or 2) See previous months or 3)'quit' to quit: """)
    if user_option == '1':
        print(f"\nAdding spending tracker for current month of {CURRENT_MONTH}\n")
        expense_tracker(CURRENT_MONTH)
        asset_tracker(CURRENT_MONTH)
        cash_flow()
    elif user_option == '2':
        see_month_finance()
        # if monthly_finance:
        #     for key, value in monthly_finance.items():
        #         print(f"The month of {key} had cash flow of ${value}")
        # else:
        #     print("No month recorded yet")
    elif user_option == 'quit':
        break
    else:
        print("Choose valid option")



