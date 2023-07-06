available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {} #create empty dictionary
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            #already in so remove
            print(f"Removing {current_choice}")
            computer_parts.pop(current_choice)
        else:
            #addng 
            print("Adding {}".format(chosen_part))
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains {computer_parts}")
    
    else:
        for key, value in available_parts.items():
            print(f"{key} {value}")

    current_choice = input("> ")

