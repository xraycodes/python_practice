import random

#word  
#get length of word
listOfWords = ['juice', 'wine', 'plain', 'whiskey']
gameWord = random.choice(listOfWords)
lengthOfWord = len(gameWord)

counter = 0

#7 guesses total, shape in object
hangmanShape = {
    "1": 'O',
    "2": '|',
    "3":"'",
    "4":"   '",
    "5":'|',
    "6": '/',
    "7": "\\"
}
hangmanResult = ' '
#if guess in word, add the word. if not then add to person

while counter < 7:
    print(f"The word is {lengthOfWord} letters long")
    guess = input("Whats the guess? ")
    if guess in gameWord:
        print(f"You win you guessed in {counter} tries.")
    else:
        counter += 1
        hangmanResult += hangmanShape[str(counter)] + '\n'
    print(hangmanResult)

#if word found before 7 you win