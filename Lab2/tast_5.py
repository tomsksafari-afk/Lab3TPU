import timeit

parts = [
    "Имя: ", "Анна", "; возраст: ", "25",
    "; город: ", "Казань", "; профессия: ", "инженер",
    "; опыт: ", "3 года", "; статус: ", "активна",
]

def concat():
    return (
        parts[0] + parts[1] + parts[2] + parts[3] +
        parts[4] + parts[5] + parts[6] + parts[7] +
        parts[8] + parts[9] + parts[10] + parts[11]
    )

def format_method():
    return "Имя: {}; возраст: {}; город: {}; профессия: {}; опыт: {}; статус: {}".format(
        "Анна", "25", "Казань", "инженер", "3 года", "активна"
    )

def f_string():
    name, age, city = "Анна", "25", "Казань"
    job, experience, status = "инженер", "3 года", "активна"
    return (
        f"Имя: {name}; возраст: {age}; город: {city}; "
        f"профессия: {job}; опыт: {experience}; статус: {status}"
    )

for name, func in [
    ("Конкатенация", concat),
    (".format()", format_method),
    ("f-строка", f_string),
]:
    t_func = timeit.timeit(func, number=500_000)
    print(f"{name}: {t_func} с")
