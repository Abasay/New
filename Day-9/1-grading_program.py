student_scores = {
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Nevielle": 62
}
student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
       student_grades[key] = "Ountstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
       student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
       student_grades[key] = "Acceptable"
    else:
       student_grades[key] = "Fail"

print(student_grades)