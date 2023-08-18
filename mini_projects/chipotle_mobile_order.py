#chipotle online ordering system emulation

#Database
TAX = 0.13
    #Lists of food criteria(Protein, Rice, Beans, Sauce, Extra
protein = 'Chicken', 'Steak', 'Barbacoa', 'Sofrita'
rice = ['Brown rice', 'White rice']
beans = ['Pinto', 'Black']
extra = ['Veggies', 'Lettuce', 'Cheese', 'Corn']
sauce = ['Mild', 'Medium', 'Hot', 'Queso']
user_order = []
    #Dictionary(Key=User_name, Value = Chosen order as a list)
user_name_order = {}

#Functions
def food_iteration(list):
    for index, _ in enumerate(list):
       print((index + 1), _)


# Main Code
user_name = input("Who is this order for?: ")

food_iteration(protein)
protein_choice = int(input("Choose your protein. "))
user_order.append(protein[protein_choice - 1])

food_iteration(rice)
rice_chooice = int(input("Choose your rice."))
user_order.append(rice[rice_chooice - 1])

food_iteration(beans)
beans_choice = int(input("Choose your beans. "))
user_order.append(beans[beans_choice - 1])

food_iteration(extra)
extra_chooice = int(input("Choose your rice."))
user_order.append(extra[extra_chooice - 1])

food_iteration(sauce)
sauce_choice = int(input("Choose your protein. "))
user_order.append(sauce[sauce_choice - 1])

user_name_order[user_name] = user_order


new = ','.join(user_order)
print(f"Order for {user_name} is {new}")




