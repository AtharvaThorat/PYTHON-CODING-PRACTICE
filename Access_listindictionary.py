#Access the value of list in a dictionary
Harry = {
    "name": "Harry",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
John = {
    "name": "John",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
Simon = {
    "name": "Simon",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [Harry,John,Simon]

for student in students:
    print (student['name'])
    print (student['homework'])
    print (student['quizzes'])
    print (student['tests'])
