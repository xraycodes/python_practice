class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and am {self.color}")

    def speak(self):
        print('meow')

class Dog(Pet):
    def speak(self):
        print('bark')

class Fish(Pet):
    pass


p = Pet('Tim', 19)
p.show()

c = Cat("Bill", 34, 'pink')
c.show()
c.speak()

d = Dog("Jill", 25)
d.show()
d.speak()

f = Fish('Bubbles', 10)
f.speak()