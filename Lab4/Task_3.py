squares_loop = []

for number in range(101):
    if number % 2 == 0:
        squares_loop.append(number ** 2)
print(squares_loop)



squares_comp = [number**2 for number in range(101) if number % 2 == 0]
print(squares_comp)



print(squares_loop == squares_comp)