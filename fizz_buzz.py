def fizz_buzz(number: int) -> str:
    """
    Function that returns fizz, buzz, fizz buzz, or the number

    Params: 
        number: user inputs a `int` and the function will play the game
        upto and including the inputted `int`
    Returns:
        Returns fizz if divisible by 3
        Returns buzz if divisible by 5
        Returns fizz buzz if divisible by 3 and 5
        Returns number if not divisible by any mentioned above
    """
    if number % 15 == 0:
        return 'fizz buzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return str(number)
        

input("Fizzbuzz.. Press enter to start ")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break   
else:
    print("Well done you reached {}".format(next_number))

