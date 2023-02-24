




#Describe what the game is about, how to play
def intro():
    print("Welcome to game of tic tac toe")
    input("Print enter to play ")

#Describe player is X or O
def players():
    while True:
        player1 = input("Would you like to be player X or O: ").upper()
        if player1 == "X":
            player1 = "X"
            print ("You are X and computer is O")
            break
        elif player1 == "O": 
            player1 = "O"
            print("You are O and computer is X")
            break
        else:
            print("Please choose either X or O")
            continue


#Print tile

#let players pick selection on board, if 3 horizontal, vertical or across then player win

#print outcome of winner

def main():
    intro()
    players()

main()