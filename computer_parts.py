computer_parts = [
    ("Keyboard", 120),
    ("Monitor", 200),
    ("Graphics card", 700),
    ("Speakers", 100),
    ("Mouse", 50),
]

while True:
    for index, (parts,price) in enumerate(computer_parts):
        print("{}: Parts: {}, Price: ${} ".format(index +1, parts, price))

    choice = int(input("What would you like to purchase? 1,2,3,4,5 "))
    if 1 <= choice <= len(computer_parts):
        item = computer_parts[choice -1][0]
        print("You have selected {} for price of ${}".format(item, computer_parts[choice -1][1]))
    else:
        break
    
    quantity = int(input("How many would you like to purchase? "))
    print("The final price of {} in quantity of {} is ${}".format(item, quantity, ((computer_parts[choice -1][1]) * quantity)))
    print("=" * 40)



