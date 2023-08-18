#chipotle online ordering system emulation

#Database
TAX = 0.13
    #Lists of food criteria(Protein, Rice, Beans, Sauce, Extra
extra = ['Veggies', 'Lettuce', 'Cheese', 'Corn']
sauce = ['Mild', 'Medium', 'Hot', 'Queso']
user_order = []

protein = {'Chicken' : 7, 'Steak' : 8, 'Barbacoa': 7, 'Sofrita': 7}
rice = {'Brown rice' : 3, 'White rice' : 3}
beans = {'Pinto' : 1, 'Black' : 1}
# extra = {'Veggies': 0, 'Lettuce'}


    #Dictionary(Key=User_name, Value = Chosen order as a list)
user_name_order = {}

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

food_iteration(protein)
protein_choice = int(input("Choose your protein. "))
user_order.append(protein[protein_choice - 1])
print(f"Adding {protein[protein_choice - 1]}\n")

food_iteration(rice)
rice_choice = int(input("Choose your rice."))
user_order.append(rice[rice_choice - 1])
print(f"Adding {rice[rice_choice- 1]}\n")


food_iteration(beans)
beans_choice = int(input("Choose your beans. "))
user_order.append(beans[beans_choice - 1])
print(f"Adding {beans[beans_choice - 1]}\n")

food_iteration(extra)
extra_choice = int(input("Choose your extras."))
user_order.append(extra[extra_choice - 1])
print(f"Adding {extra[extra_choice - 1]}\n")

food_iteration(sauce)
sauce_choice = int(input("Choose your sauce. "))
user_order.append(sauce[sauce_choice - 1])
print(f"Adding {sauce[sauce_choice - 1]}\n")

user_name_order[user_name] = user_order


new = ','.join(user_order)
print(f"Order for {user_name} is {new}")

for i in user_order:
    if i in proteins:
        print(proteins[i])
    elif i in rices:
        print(rices[i])




