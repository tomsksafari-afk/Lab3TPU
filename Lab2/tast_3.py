# Создаем исходную строку с пробелами и разным регистром
s = "  Hello, WoRLD!  "
print("Исходная строка:", s, "id:", id(s))

# Применяем strip()
s1 = s.strip()
print("После strip():", s1, "id:", id(s1))

# Применяем lower()
s2 = s1.lower()
print("После lower():", s2, "id:", id(s2))

# Применяем replace()
s3 = s2.replace("world", "universe")
print("После replace():", s3, "id:", id(s3))
