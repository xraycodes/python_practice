name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input("You are on a dirt road, it has come to an end, you can go left or right. Which way would you like to go? ").lower()
 
if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to across " )

    if answer == 'swim':
        print('You swam across, and eaten by alligator')
    elif answer =='walk':
        print('You walked for many miles, ran out of water and lost the game')
    else:
        print('not a valid option. You lose')
elif answer == 'right':
    answer = input("You come to a bridge, looks wobbly, do you want to cross or head back(cross/back)")
    
    if answer == 'back':
        print('You go back and lose')
    elif answer =='cross':
        answer = input('you cross the bridge and meet a stranger, do you talk to them? (yes/no)')
        if answer =='yes':
            print("You got gold and you win")
        elif answer =='no':
            print("You ignored the stranger and they are offended and you lose")
        else:
            print('not a valid answer')
    else:
        print('not a valid option. You lose')
else:
    print('Not a valid option. You lose.')

print(f"Thanks for trying {name}")