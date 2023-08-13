# Program designed to keep track of monthly expenses
# Calculates Cash Flow (Money going out, in, net)

from datetime import datetime

#CONSTANTS
CURRENT_MONTH = datetime.now().strftime("%B")

# Database
    # Monthly spending. Dictionary(Key: Month, Value: Spendings)
monthly_expenses = {}
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
def expense_tracker():
    while True:
        print("Write the expenses from the month, type quit when finished")
        expense = input("What's the name of the expense?: ")
        if expense == 'quit':
            break
        expense_amount = int(input(f"How much did {expense} cost?: $"))
        expenses[expense] = expense_amount

def asset_tracker():
    while True:
        print("Write the asset from the month, type quit when finished")
        asset = input("Whats the name of the asset?: ")
        if asset == 'quit':
            break
        asset_amount = int(input(f"How much was the {asset} aquired?: $"))
        assets[asset] = asset_amount

def cash_flow():
    for expense_sum in expenses.values():
        expense_total = 0 
        expense_total += expense_sum
    
    for asset_sum in assets.values():
        asset_total = 0
        asset_total += asset_sum

    print("#"*80)
    print(f"The total liability for the month of {CURRENT_MONTH} was ${expense_total}")
    print(f"The total asset for the month of {CURRENT_MONTH} was ${asset_total}")
    net = asset_total - expense_total
    print(f"The total net income for the month of {CURRENT_MONTH} was {net}")
    monthly_expenses[CURRENT_MONTH] = net


#Main Code

while True:
    user_option = input(
    """Choose option 1 to add tracker for current month or 2) See previous months or 3)'q' to quit: """)
    if user_option == '1':
        print("#"*80)
        print(f"Adding spending tracker for current month of {CURRENT_MONTH}")
        expense_tracker()
        asset_tracker()
        cash_flow()
    elif user_option == '2':
        if monthly_expenses:
            for key, value in monthly_expenses.items():
                print(f"The month of {key} had cash flow of ${value}")
        else:
            print("No month recorded yet")
    elif user_option == 'q':
        break
    else:
        print("Choose valid option")


