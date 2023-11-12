entireQuiz = {
    "number": 1,
    "question": "What is 5 + 1?",
    "choices": {'a': 5, 'b':6, 'c':3, 'd':9},
    "correct": 'b'
}


print(f"""
Quiz number {entireQuiz['number']}
{entireQuiz['question']}
{entireQuiz['choices']}
""")

while True:
    playerGuess = input("Your answer? ")
    if playerGuess == entireQuiz["correct"]:
        print("You are right")
        break
    else:
        print('Try again')