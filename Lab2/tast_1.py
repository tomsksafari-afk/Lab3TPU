a = 1000
b = 1000

print(a == b)
print(a is b) # Может быть False, т.к. это разные объекты в памяти
print()

str1 = "hello"
str2 = "hello"

print(str1 == str2)
print(str1 is str2) # Обычно True, потому что Python использует пул строк для коротких строк
print()

long_str1 = "a" * 1000
long_str2 = "a" * 1000

print(long_str1 == long_str2)
print(long_str1 is long_str2) # Возможно False, т.к. они не обязательно один и тот же объект



# Пример 1
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # True
print(x is y) # False, разные объекты в памяти
print()

# Пример 2
a = (4, 5)
b = (4, 5)

print(a == b) # True
print(a is b) # False, разные объекты в памяти, но у меня True



x = None

print(x is None) # Правильный способ проверки, т.к. None — это единственный экземпляр

print(x == None) # Можно, но не рекомендуется
