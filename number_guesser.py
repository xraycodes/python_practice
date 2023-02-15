import random

top_of_range = input('Please put a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please print a number higher than 0 next time")
        quit()
else:
    print("Please print a number next time")
    quit()

random_number = random.randint(1, top_of_range)
counter = 0

while True:
    counter += 1
    user_guess = (input('Guess the number: '))

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Print a valid number")
        continue

    if user_guess > random_number:
        print("guess again, too high")
    elif user_guess < random_number:
        print("Too low, guess again")
    else:
        print(f"you guessed correctly, the number was {random_number} and got it in {counter} times")
        break