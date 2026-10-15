# Кортеж с постоянными правилами выдачи
library_rules = ("Техно", 21, 5)

# Список заявок в порядке поступления
book_requests = [501, 507, 512, 526, 531, 544]

# Множество читателей с задолженностью
debtors = {507, 526, 544}

# Словарь книг по инвентарному номеру
books = {
    "B-101": "Чистый код",
    "B-102": "Алгоритмы",
    "B-103": "Python для начинающих",
    "B-104": "Базы данных"
}

# Вывод правил
print(
    f"Правила выдачи: библиотека «{library_rules[0]}», "
    f"{library_rules[1]} день, "
    f"не более {library_rules[2]} книг"
)

# Вывод заявок
print("Заявки в порядке поступления:", *book_requests, sep=", ")

# Вывод должников
print("Читатели с задолженностью:", *debtors, sep=", ")

# Вывод книг
print("Книги:")
for number, title in books.items():
    print(f"{number} - «{title}»")

# Добавляем новую заявку
book_requests.append(558)

print("После добавления заявки:", *book_requests, sep=", ")

# Проверяем задолженность читателя
reader = 526

if reader in debtors:
    print(f"Читатель {reader} имеет задолженность: да")
else:
    print(f"Читатель {reader} имеет задолженность: нет")

# Получаем книгу по инвентарному номеру
inventory_number = "B-102"

print(
    f"Книга с номером {inventory_number}: "
    f"«{books[inventory_number]}»"
)
