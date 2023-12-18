top = ["", "", ""]
middle = ["", "", ""]
bottom = ["", "", ""]
players = ['player1', 'player2']
player1 = 'X'
player2 = 'O'
count = 0
Game = False

def playerInput():
    row = int(input("For row, 0 for top, 1 for middle, 2 for bottom "))
    column = int(input("For column, 0 for left, 1 for middle, 2 for right "))
    
def winTiles():
    if top[0] == top[1] == top[2] or middle[0] == middle[1] == middle[2] or bottom[0] == bottom[1] == bottom[2]:
        return 'You win'
    elif top[0] == middle[0] == bottom[0] or top[1] == middle[1] == bottom[1] or top[2] == middle[2] == bottom[2]:
        return 'You win'
    elif top[0] == middle[1] == bottom[2] or top[2] == middle[1] == bottom[0]:
        return 'You win'
        
def checkTileTaken(grid, selection,player):
    if grid == 0:
        if top[selection]:
            print("Spot taken, choose again")
            return 0
        else:
            top[selection] = f"{player}"
            return 1
        
    elif grid == 1:
         if top[column]:
            top[column] = f"{player}"
    elif grid == 2:
         if top[column]:
            top[column] = f"{player}"

    else:
            print("Spot taken")
    

while Game == False:
    count += 1
    for i in players:
        if i == 'player1':
            print(f"{i} {player1} turn")
            row = int(input("For row, 0 for top, 1 for middle, 2 for bottom "))
            column = int(input("For column, 0 for left, 1 for middle, 2 for right "))
            
            if row == 0:
                result = checkTileTaken(row,column, player1)
                print(result)
                if result == 0:
                    playerInput()
                    result = checkTileTaken(row,column, player1)
                    if result == 1:
                        continue
            if row == 1:
                checkTileTaken(row,column, player1)
                middle[column] = 'O'
            if row == 2:
                checkTileTaken(row,column, player1)
                bottom[column] = 'O'

    
                
        if count >= 3:
            winner = winTiles()
            if winner == 'You win':
                print("Player 1 wins")
                Game = True
                break
            
        if i == 'player2':
            print(f"{i} {player2} turn")
            row = int(input("For row, 0 for top, 1 for middle, 2 for bottom "))
            column = int(input("For column, 0 for left, 1 for middle, 2 for right "))
            
            if row == 0:
                top[column] = 'O'
            if row == 1:
                middle[column] = 'O'
            if row == 2:
                bottom[column] = 'O'
            
        if count >= 3:
            winner = winTiles()
            if winner == 'You win':
                print("Player 2 wins")
                Game = True
                break
        
        board = f"{top}\n\n{middle}\n\n{bottom}"
        print(board)
        
board = f"{top}\n\n{middle}\n\n{bottom}"       
print(board)
