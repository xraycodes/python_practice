import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("enter valid choices")
        continue

    random_number = random.randint(0,2) 
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}")

    if user_input == 'rock' and computer_pick == 'scissors':
        print('you win')
        user_wins += 1 
        continue

    elif user_input == 'paper' and computer_pick == 'rock':
        print('you win')
        user_wins += 1 
        continue

    elif user_input == 'scissors' and computer_pick == 'paper':
        print('you win')
        user_wins += 1 
        continue

    elif user_input == computer_pick:
        print("you tied")
        continue
    
    else:
        computer_wins += 1
        print('you lose')

print(f"You won {user_wins} times while computer won {computer_wins}")
print("goodbye")