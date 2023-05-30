available_parts = ['quit','computer', 'monitor', 'keyboard', 'mouse', 'mouse pad']
current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in '12345':
        print('adding {}'.format(current_choice))
         
    else:
        print("Please add from the list")
        for number,part in enumerate(available_parts):
            print("{}:{}".format(number,part))
    current_choice = input()
