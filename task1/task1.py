students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

mean_grades = {
    student["name"]: sum(student["grades"]) / len(student["grades"])
    for student in students
}

print(mean_grades)
print("Студент с наивысшей средней оценкой:", max(mean_grades, key=mean_grades.get))
