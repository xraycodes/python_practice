file = "flowers.txt"
li = ['pizza', 'chicken', 'beer', 'food', 'burger', 'fries']

with open(file, 'w') as flower:
    for i in li:
        flower.write(i)
        flower.write(str(7))
