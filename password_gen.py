import random

CHAR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ''

#how many lengths
while True:
    print(f"Available chacters: {CHAR}")
    length = input("How many length do you want the password?: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Please write correct number of length")

for i in range(length):
    password_gen = random.randint(0,(len(CHAR) - 1))
    password += CHAR[password_gen]

print(password)

print("Password must contain one upper, one lower, and one special sign")
for char in password:
    print(char)
    if char.isupper() == False:
        print("Requires capitalized letters")
    elif char.islower() == False:
        print("requires non capitalized letters")
    else:
        print("password is fine")


