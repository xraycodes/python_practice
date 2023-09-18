OPERATOR = ["+", "-", "*", "/"]
currentValue = 0
#function that takes in operator as parameter, and 2 number inputs

def calculation(num1, num2, operator):
    if operator == '+':
        return num1 + num2 
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 0
        return num1 / num2

def choose_operator():
    while True:
        operator = input("Choose what operation you want to perform(+ , -, *, /) ")
        if operator in OPERATOR:
            return operator
        else:
            print("Choose valid operator")

#input user number 1 
#input user number 2
#input operator 

firstOperandValid = secondOperandValid = False
while True:
    if firstOperandValid and secondOperandValid == True:
            break
    firstOperand = input("What's the first number? ")
    if firstOperand.isdigit():
        firstOperand = int(firstOperand)
        firstOperandValid = True
    else:
        print("Please enter valid first number")
        continue

    while True:
        secondOperandValid = False
        secondOperand = input("What's the second number? ")
        if secondOperand.isdigit():
            secondOperand = int(secondOperand)
            secondOperandValid = True
        else:
            print("Please enter valid second number")
        if firstOperandValid and secondOperandValid == True:
            break

operator = choose_operator()
answer = calculation(firstOperand, secondOperand, operator)
if answer == 0:
    print("Unable to divide number by 0")
else:
    currentValue += answer
    print(answer)
