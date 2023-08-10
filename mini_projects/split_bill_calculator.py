

# how many people have ordered
# how much each item was for the individual
    #Dictionary: Key: Name, Value: Price
# Create calculation including tax and tip, delivery cost, other expenses(entered by user)
#Tell how much each indiviudal owes
    #Item total = individual_item + tax + other expenses/number of diners

TAX = 1.13
fee_total = 0
orders = {}
fees = {}


def calculation(meal_cost, fee, TAX):
    cost = (meal_cost * TAX) + (fee/number_of_diners)
    return cost


#Main code
number_of_diners = int(input("How many diners for this order? "))

for individual in range(number_of_diners):
    name = input(f"Enter the name of individual #{individual +1}: ")
    cost = int(input(f"How much was the meal for {name}? $"))
    orders[name] = cost

print('*' * 80)
while True:
    print('Type q when finished entering')
    charge_information = input("What other charges/fees were made?(Delivery, service, etc) ")
    if charge_information == 'q':
        break
    other_charges = int(input(f"Enter the amount for the following fee:{charge_information}: $"))
    fees[charge_information] = other_charges
    
   
for serivce_fees, value in fees.items():
    fee_total += value
print(fee_total)

print('*' * 80)
print("The price for everybody are as follows:")
for name, price_of_meal in orders.items():
    individual_cost = calculation(price_of_meal, fee_total, TAX)
    print(f"The cost of {name} is ${individual_cost:.2f}")
    







    