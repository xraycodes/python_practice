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
        

number_request = int(input("What number do you want to play until? "))
for i in (range(1,number_request + 1)):
    print(fizz_buzz(i))

