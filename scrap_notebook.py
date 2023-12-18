for i in range(10):
    print(f"First number {i}")
    guess = int(input('wat number'))
    for i in range(10):
        print(f"Second number {i}")
        if i == 1:
            if guess == 1:
                continue
        else:
            print('wag')