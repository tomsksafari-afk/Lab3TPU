names = ["Анна", "Иван", "Мария", "Пётр"]
grades = [5, 4, 5, 3]

for name, grade in zip(names, grades):
    print(f"{name}: {grade}")