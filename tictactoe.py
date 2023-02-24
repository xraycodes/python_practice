ROW = 3 
COLUMN = 3
BOARD = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",
        ]   

currentPlayer = "X"
winner = None
gameRunning = True



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

def printBoard(board):
   print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
   print("_________")
   print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
   print("_________")
   print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])


#let players pick selection on board, if 3 horizontal, vertical or across then player win
def playerInput(board):
    while True:
        inp = int(input("Enter a number 1-9: "))
        if 1 <= inp <=9 and BOARD[inp-1] == "-":
            board[inp-1] = currentPlayer
        else:
            print("Spot already taken")
        return board

#check win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
#print outcome of winner

def main():
    intro()
    players()
    update = playerInput(BOARD)
    checkDiag(update)
    checkHorizontal(BOARD)
    checkVertical(BOARD)
    checkTie(BOARD)
    print(winner)




main()