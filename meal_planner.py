from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    # if item in data: 
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount

display_dict = {}
shopping_list = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 20)
    for key, value in display_dict.items():
        print(f"{key} - {value}")
     
    choice = input(": ")

    if choice == "0":
        break 
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingridients...")
        ingridients = recipes[selected_item]
        print(ingridients)

        for food_item, required_quantity in ingridients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
       
for things in shopping_list.items():
    print(things)