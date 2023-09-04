import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number has to be between 2-4")
    else:
        print("Please print valid number")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} turn has just started")
        print(f"Player {player_idx + 1} current score is {players_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y)? ")
            if should_roll.casefold() != 'y':
                break

            value = roll()
            if value == 1:
                print(f"You rolled a {value}")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            
            print(f"Your current score is {current_score}")
        
        players_scores[player_idx] += current_score
        print(f"Your total score is: {players_scores[player_idx]}")

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"The winner is player {winning_idx + 1} with score of {max_score}")