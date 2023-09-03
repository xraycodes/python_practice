class Course():
    number_of_students = 0

        
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = 'human'
        Course.number_of_students += 1

    @classmethod
    def speak(self):
        return 'hello'

class Student(Course):
    def __init__(self, name, age, gender, degree):
        super().__init__(name,age,gender)
        self.degree = degree

class SpecialNeeds(Course):
    def __init__(self, name, age, gender, needs):
        super().__init__(name,age,gender)
        self.needs = needs
        SpecialNeeds.number_of_students = 0

Brian = Student('Brian', 29, 'Male', 'Science')
Darryl = SpecialNeeds('Darryl', 15, 'Male', 'Autism')

print(Course.speak())