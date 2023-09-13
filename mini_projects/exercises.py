#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


userNumber = int(input("Choose a number "))

numbers = list(range(1,userNumber + 1))
divisors = []

for number in numbers:
    if userNumber % number == 0:
        divisors.append(number)

print(divisors)
