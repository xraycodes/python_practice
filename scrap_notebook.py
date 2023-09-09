MAX = 100

for number in range(1,MAX):
    guess = input("What's the next number? ")
    if number %3 == 0:
        if guess != 'c':
            break
    elif guess == str(number):
        continue
    else:
        break

print('You lose')