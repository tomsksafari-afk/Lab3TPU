students = [
    {"name": "Anna", "score": 85, "attempts": 2},
    {"name": "Ivan", "score": 55, "attempts": 1},
    {"name": "Maria", "score": 90, "attempts": 4},
    {"name": "Peter", "score": 70, "attempts": 3},
    {"name": "Olga", "score": 60, "attempts": 2}
]

# Способ 1: обычный цикл с append()
passed_loop = []

for student in students:
    if student["score"] >= 60 and student["attempts"] <= 3:
        passed_loop.append(student["name"])

print(passed_loop)


# Способ 2: list comprehension
passed_comp = [student["name"] for student in students if student["score"] >= 60 and student["attempts"] <= 3]

print(passed_comp)



print(passed_loop == passed_comp)