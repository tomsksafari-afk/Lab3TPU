grades = [5, 4, 3, 5, 4]

# Способ 1: ручной счётчик
print("Ручной счётчик:")

number = 1

for grade in grades:
    print(number, grade)
    number += 1


print()
print("enumerate():")

for number, grade in enumerate(grades, start=1):
    print(number, grade)