#chipotle online ordering system emulation

#Database
TAX = 0.13
user_order = []
chosen_food_list = []
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
def food_iteration(data):
    if isinstance(data, dict):
        for index, key in enumerate(data):
            print((index + 1), key)
    if isinstance(data, list):
        for index, _ in enumerate(data):
            print((index + 1), _)


def item_price():
    pass


# Main Code
user_name = input("Who is this order for?: ")
user_name_order[user_name] = 0

while True:
    for index, (key, value) in enumerate(food['Protein'].items()):
        print(index + 1, key)
    proteins_list = list(food['Protein'].keys())
    user = int(input("What's your choice of protein?(In Numbers): "))
    if 1 <= user <= len(food['Protein']):
        chosen_protein = proteins_list[user - 1]
        user_order.append(chosen_protein)
        user_name_order[chosen_protein] = {'price' : food['Protein'][chosen_protein]}
    else:
        print('Number out of range, Try again')

    for index, (key, value) in enumerate(food['Rice'].items()):
        print(index + 1, key)
    rice_list = list(food['Rice'].keys())
    user = int(input("What's your choice of rice?(In Numbers): "))
    if 1 <= user <= len(food['Rice']):
        chosen_rice = rice_list[user - 1]
        user_order.append(chosen_rice)
        user_name_order[chosen_rice] = {'price': food['Rice'][chosen_rice]}
        break
    else:
        print('Number out of range, Try again')
        break

print(user_name_order)


# food_iteration(protein)
# protein_choice = int(input("Choose your protein. "))
# user_order.append(protein[protein_choice - 1])
# print(f"Adding {protein[protein_choice - 1]}\n")




