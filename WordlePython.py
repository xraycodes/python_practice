#https://realpython.com/python-wordle-clone/#step-2-use-a-word-list

WORD = "SNAKE"


for i in range(1,7):
    guess = input("Word?: ").upper()
    if guess == 'SNAKE':
        print("Correct")
        break
    
    correct_letters = {
        letter for letter, correct in zip(guess,WORD) if letter == correct
    }
    misplaced_letters = set(guess) & set(WORD) - correct_letters
    wrong_letters = set(guess) - set(WORD)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
    
