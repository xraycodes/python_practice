class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

        
kenwood = Kettle("Kenwood", 99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print(f"Models: {kenwood.make},price = {kenwood.price}, {hamilton.make}, price={kenwood.price} ")
