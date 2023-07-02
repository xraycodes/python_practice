numbers = (0, 1, 2, 3, 4, 5)

# print(numbers[0][1], sep=";")
# print(*numbers, sep=";")
# print(0,1,2,3,4,5, sep=";")

def test_star(h,*args):
    print(args)
    new = *args
    print(*args)
    print(h)
    print(new)
    for x in args:
        print(x)
  
       


test_star('hello',0,1,2,3,4,5)

