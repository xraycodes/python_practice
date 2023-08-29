class Pet:   #general class
    def __init__(self, name, age):
        self.name = name
        self. age = age

    def show(self):
        print(f"I am {self.name} and am {self.age} years old")

class Cat(Pet):  #More specific class/child
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
        
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.show()

c= Cat("Bill", 34)
c.show()
c.speak()

d= Dog("Jill", 25)
d.show()
d.speak()