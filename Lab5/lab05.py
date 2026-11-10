from typing import TypedDict


# ============================================================
# 01. Подготовительный эксперимент: аргументы и объекты
# ============================================================

def change_list(values):
    print("Внутри change_list до:", values, "id:", id(values))
    values.append(4)
    print("Внутри change_list после:", values, "id:", id(values))


def change_string(text):
    print("Внутри change_string до:", text, "id:", id(text))
    text = "new text"
    print("Внутри change_string после:", text, "id:", id(text))


def change_number(number):
    print("Внутри change_number до:", number, "id:", id(number))
    number = 100
    print("Внутри change_number после:", number, "id:", id(number))


print("=== Эксперимент со списком ===")
numbers = [1, 2, 3]
print("До вызова:", numbers, "id:", id(numbers))
change_list(numbers)
print("После вызова:", numbers, "id:", id(numbers))

print()

print("=== Эксперимент со строкой ===")
text = "hello"
print("До вызова:", text, "id:", id(text))
change_string(text)
print("После вызова:", text, "id:", id(text))

print()

print("=== Эксперимент с числом ===")
number = 10
print("До вызова:", number, "id:", id(number))
change_number(number)
print("После вызова:", number, "id:", id(number))

print()


# ============================================================
# 02. Практикум по вариантам — вариант 2
# ============================================================

def delivery_cost(distance, /, rate=10, *, base=0):
    return distance * rate + base


def multiply_sizes(*sizes):
    result = 1

    for size in sizes:
        result *= size

    return result


def delivery_card(city, **fields):
    card = {"city": city}
    card.update(fields)
    return card


# 9 готовых проверок

assert delivery_cost(5) == 50
assert delivery_cost(5, 20) == 100
assert delivery_cost(5, rate=20, base=30) == 130

assert multiply_sizes() == 1
assert multiply_sizes(4) == 4
assert multiply_sizes(2, 3, 4) == 24

assert delivery_card("Томск") == {"city": "Томск"}
assert delivery_card("Томск", paid=True) == {
    "city": "Томск",
    "paid": True,
}
assert delivery_card("Северск", street="Мира", house=5) == {
    "city": "Северск",
    "street": "Мира",
    "house": 5,
}


# 4 собственные проверки

# А — второй параметр передан по позиции
assert delivery_cost(10, 15) == 150

# А — второй параметр передан по имени
assert delivery_cost(10, rate=15) == 150

# Б
assert multiply_sizes(5, 2, 3) == 30

# В
assert delivery_card("Томск", paid=True, price=500) == {
    "city": "Томск",
    "paid": True,
    "price": 500,
}


# Ошибочные вызовы.
# Первый параметр нельзя передать по имени, потому что он находится
# перед символом /.

# delivery_cost(distance=5)

# Последний параметр base нельзя передать по позиции,
# потому что он находится после символа *.

# delivery_cost(5, 10, 20)


# ============================================================
# 03. Основная задача — вариант 2
# Распределение заказов
# ============================================================

class Order(TypedDict):
    number: int
    city: str
    paid: bool


def move_orders(
    source: list[Order],
    destination: list[Order],
    cities: set[str],
) -> list[Order]:
    """Перенести оплаченные заказы из обслуживаемых городов."""
    remaining = []

    for order in source:
        if order["city"] in cities and order["paid"]:
            destination.append(order)
        else:
            remaining.append(order)

    source[:] = remaining

    return destination


# ============================================================
# 04. Тесты основной функции
# ============================================================


def test_one_matching_order() -> None:
    """Одна подходящая запись переносится."""
    a: Order = {"number": 1041, "city": "Томск", "paid": True}
    b: Order = {"number": 1042, "city": "Северск", "paid": False}

    source = [a, b]
    destination: list[Order] = []

    result = move_orders(source, destination, {"Томск"})

    assert source == [b]
    assert destination == [a]
    assert result is destination


def test_several_matching_orders() -> None:
    """Несколько подходящих записей переносятся в исходном порядке."""
    a: Order = {"number": 1041, "city": "Томск", "paid": True}
    b: Order = {"number": 1042, "city": "Северск", "paid": True}
    c: Order = {"number": 1043, "city": "Томск", "paid": True}
    d: Order = {"number": 1044, "city": "Кедровый", "paid": False}

    source = [a, b, c, d]
    destination: list[Order] = []

    result = move_orders(source, destination, {"Томск", "Северск"})

    assert source == [d]
    assert destination == [a, b, c]
    assert result is destination


def test_no_matching_orders() -> None:
    """Если подходящих заказов нет, списки не меняются."""
    a: Order = {"number": 1041, "city": "Томск", "paid": False}
    b: Order = {"number": 1042, "city": "Северск", "paid": False}

    source = [a, b]
    destination: list[Order] = []

    result = move_orders(source, destination, {"Томск", "Северск"})

    assert source == [a, b]
    assert destination == []
    assert result is destination


def test_empty_source() -> None:
    """Пустой исходный список не вызывает ошибку."""
    source: list[Order] = []
    destination: list[Order] = [
        {"number": 1000, "city": "Томск", "paid": True}
    ]

    result = move_orders(source, destination, {"Томск"})

    assert source == []
    assert destination == [
        {"number": 1000, "city": "Томск", "paid": True}
    ]
    assert result is destination


def test_existing_destination() -> None:
    """Существующие записи второго списка остаются в начале."""
    a: Order = {"number": 1041, "city": "Томск", "paid": True}
    b: Order = {"number": 1042, "city": "Северск", "paid": True}
    existing: Order = {"number": 1000, "city": "Кедровый", "paid": False}

    source = [a, b]
    destination = [existing]

    result = move_orders(source, destination, {"Томск", "Северск"})

    assert source == []
    assert destination == [existing, a, b]
    assert result is destination


def test_unpaid_order_is_not_moved() -> None:
    """Неоплаченный заказ не переносится даже из обслуживаемого города."""
    a: Order = {"number": 1041, "city": "Томск", "paid": True}
    b: Order = {"number": 1042, "city": "Томск", "paid": False}

    source = [a, b]
    destination: list[Order] = []

    result = move_orders(source, destination, {"Томск"})

    assert source == [b]
    assert destination == [a]
    assert result is destination


# ============================================================
# 05. Запуск всех тестов
# ============================================================

test_one_matching_order()
test_several_matching_orders()
test_no_matching_orders()
test_empty_source()
test_existing_destination()
test_unpaid_order_is_not_moved()

print("Все проверки пройдены")