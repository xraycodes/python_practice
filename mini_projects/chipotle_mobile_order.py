#chipotle online ordering system emulation

#Database
TAX = 1.13
#Dictionary(Key=User_name, Value = Chosen order as a list)
user_name_order = {}
#Lists of food criteria(Protein, Rice, Beans, Sauce, Extra
food = {'Protein': {
            'Chicken' : 7,
            'Steak' : 8,
                    },
        'Rice': {
            'Brown rice' : 3,
            'White rice' : 3
                },
        'Beans': {
            'Pinto' : 1,
            'Black' : 1,
                },
        'Extra': {
            'Veggies' : 0,
            'Lettuce' : 0,
            'Cheese' : 0,
            'Corn' : 0,
                },
        'Sauce': {
            'Mild' : 0,
            'Medium' : 0,
            'Hot' : 0,
            'Queso' : 0,
        }
    }

#Functions
def food_iteration(data, food_type):
    """
    Iterates through `data` and its nested `food_type` and adds user order of items 
    to a empty dictionary and its associated price.

    Params:
    data: The dictionary(food) containing all the types of food(Proteins, Rice) as key
    food_type: The type of food to be iterated(Proteins, Rice, etc..) 
               which nests more specifics of food dictionary(chicken, steak...(key) and its price(value))
    """
    for index, (key,_) in enumerate(data[food_type].items()):
            print((index + 1), key)
    food_type_list = list(data[food_type].keys())
    user = int(input(f"What's your choice of {food_type}?(In Numbers): "))
    if 1 <= user <= len(data[food_type]):
        chosen_food_type = food_type_list[user - 1]
        print(f'Adding {chosen_food_type}')
        user_name_order[chosen_food_type] = food[food_type][chosen_food_type] 
        print()
    else:
        print('Number out of range, Try again')


def multiple_food_choices(data, food_type):
    """
    Iterates through `data` and its nested `food_type` and adds user order of items 
    to a empty dictionary and its associated price. Different to food_iteration function
    because this function allows user to add multiple order of items in the same category
    (Example: Extra option in the data contains veggies, lettuce, etc..)

    Params:
    data: The dictionary(food) containing all the types of food(Proteins, Rice) as key
    food_type: The type of food to be iterated(Proteins, Rice, etc..) 
               which nests more specifics of food dictionary(chicken, steak...(key) and its price(value))
    """
    for index, (key,_) in enumerate(data[food_type].items()):
        print((index + 1), key)
    food_type_list = list(data[food_type].keys())
    while True:
        user = int(input(f"What's your choice of {food_type}?(In Numbers), print '9' when done: "))
        if 1 <= user <= len(data[food_type]):
            chosen_food_type = food_type_list[user - 1]
            print(f'Adding {chosen_food_type}')
            user_name_order[chosen_food_type] = food[food_type][chosen_food_type] 
            print()
        elif user == 9:
            break
        else:
            print("Number out of range, enter valid choice")

def item_price(total=0):
    """
    Calculates the total price for users' order

    Params:
    total=0 : Fixed argument initializing the total at $0 

    Returns:
    float: The total cost of the user's food rounded to 2 decimals 
    """
    for value in user_name_order.values():
        total += value
    return round(total * TAX ,2)



# Main Code
if __name__ == '__main__':
    user_name = input("Who is this order for?: ")
    print(f"Okay! Ordering for {user_name}")
    print()

    for key in food.keys():
        if key == 'Extra' or key == 'Sauce':
            multiple_food_choices(food, key)
        else:
            food_iteration(food, key)

    order = ''
    for key in user_name_order.keys():
        order += (key + ', ')
    print(f"The order for {user_name} includes: {order}")
    print(f"The total price is ${item_price()}")






