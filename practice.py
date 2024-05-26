# https://pynative.com/python-basic-exercise-for-beginners/
userInput = input("Original string is: ")


for i in range(len(userInput)):
    if i % 2 == 0:
        print(userInput[i])
    else:
        continue