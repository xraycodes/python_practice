import random

#function that generates random number 1,6
def randomNumber():
    number = random.randint(1,6)
    return number

#2 players
playerOne = input("Name of player 1?: ")
playerTwo = input("Name of player 2?: ")


#compare the number
input("Press enter to roll the dice")
player1 = randomNumber()
player2 = randomNumber()

#print out winner
if player1 > player2:
    print("Player 1 wins")
elif player1 < player2:
    print("Player 2 wins")
else:
    print("It's a tie")