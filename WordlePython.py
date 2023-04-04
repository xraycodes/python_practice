for i in range(1,7):
    guess = input("Word?: ").upper()
    if guess == 'SNAKE':
        print("Correct")
        break
    print("False")