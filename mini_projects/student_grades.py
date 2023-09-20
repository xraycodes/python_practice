header = ['Math', 'Science', "English, 'Average Grade"]

student_info = {
    'John' : [75, 80, 91],
    'Mostafa' : [69, 77, 94],
    'Amy': [77, 84, 88],
    'Chris': [72, 81, 96],
    'Robb': [90, 80, 88],
}

courses_grade = {

    }

def averageGrade():
    for key, value in student_info.items():
        average = (sum(value)/len(value))
        print(key, average)


