# lauren cook
# jan 20, 2022
# make a gradebook!

lloyd = {
    "name" : "Lloyd",
    "homework" : [90.0, 97.0, 75.0, 92.0],
    "quizzes" : [88.0, 40.0, 94.0],
    "tests" : [75.0, 90.0],
    }

alice = {
    "name" : "Alice",
    "homework" : [100.0 , 89.0, 99.0, 67.0],
    "quizzes" : [75.0, 99.0, 65.0],
    "tests" : [100.0, 79.0],
    }

tyler = {
    "name" : "Tyler",
    "homework" : [100.0, 100.0, 100.0, 100.0],
    "quizzes" : [100.0, 99.0, 100.0],
    "tests" : [100.0, 98.0]
    }

students = [lloyd, alice, tyler]

for student in students:
    print (student)

for value, key in lloyd.items() :
    print(value, ':', key,)
    
def average(num):
    total = float(sum(num))
    avg = total / len(num)
    return avg


print("homework average", average(lloyd['homework']))
    
def get_average(student):
    homework = student["homework"]
    quizzes = student["quizzes"]
    tests = student["tests"]
    avg = average(homework)*0.1 + average(quizzes)*0.3 + average(tests)*0.6
    return avg

print("grade average", get_average(lloyd))

# get a letter grade instead of number
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Lloyd letter grade:", get_letter_grade(get_average(lloyd)))

#gets average for whole class
def get_class_average(students):
    results = []
    for pee in students:
        results.append(get_average(pee))
    return average(results)

print("class average:", get_class_average(students))
print("class average letter grade:", get_letter_grade(get_class_average(students)))