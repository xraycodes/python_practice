available_parts = ['quit', 'monitor', 'keyboard', 'mouse', 'mouse pad']
current_choice = '-'
computer_parts = []
valid_choices = []

for i in range(1,len(available_parts)):
    valid_choices.append(str(i))

while current_choice != '0':
    if current_choice in valid_choices:
        print('adding {}'.format(current_choice))
        index = int(current_choice)
        computer_parts.append(available_parts[index])
         
    else:
        print("Please add from the list")
        for number,part in enumerate(available_parts):
            print("{}:{}".format(number,part))
    current_choice = input()

if computer_parts:
    print(computer_parts)
else:
    print("You selected nothing")

