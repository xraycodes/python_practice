#add
def add(a,b):
    return (a + b)

#subtract
def subtract(a,b):
    return (a - b)

#multiply
def multiply(a,b):
    return (a * b)

#divide
def divide(a,b):
    return (a / b)

def main():
    while True:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        operation = input("What operation would you like to perform? (+,-,*,/): ") 
        if operation == '+':
            output = add(num1,num2)
            break
        elif operation == '-':
            output = subtract(num1,num2)
            break
        elif operation == '*':
            output = multiply(num1,num2)
            break
        elif operation == '/':
            output = divide(num1,num2)
            break
        else:
            print("Print correct operation to perform")
    print(output)

    redo = input('Would you like to make another calculation? (y/n):')
    if redo == 'y':
        main()
    else:
        quit

main()


