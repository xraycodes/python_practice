def factorial(number: int)-> int:
    """
    Produces the factorial product of number

    params: number
    returns: factorial of the number
    """
    for value in (range(0,number + 1)):
        factorial_product = 1
        for factorial in range(1,value  + 1):
            factorial_product  *= factorial    
    return factorial_product


for index, i in enumerate(range(36)):
    print(index, factorial(i))