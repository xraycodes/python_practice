def factorial(n):
    # n! can also be defined as n * (n-1)!
    """Calcualtes n! recursively"""
    if n <= 1:
        return 1
    else:
        # print(n/0)
        return n * factorial(n-1)

try:  
    print(factorial(9))
except RecursionError:
    print("This program cannot calculat facotiral that large")
except ZeroDivisionError:
    print("Cannot divide by 0")
else:
    print("nice")
finally:
    print("The finally clause always executes")

print("Program termianting")