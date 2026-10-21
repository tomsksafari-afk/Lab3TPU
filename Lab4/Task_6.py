import time

sizes = [10_000, 100_000, 1_000_000]
runs = 7

for size in sizes:
    numbers = list(range(size))



    def using_append():
        result = []
        for number in numbers:
            if number % 2 == 0:
                result.append(number ** 2)
        return result



    def using_comprehension():
        return [number ** 2 for number in numbers if number % 2 == 0]

    append_times = []
    comprehension_times = []



    for i in range(runs):
        start = time.time()
        using_append()
        append_times.append(time.time() - start)

        start = time.time()
        using_comprehension()
        comprehension_times.append(time.time() - start)



    append_average = sum(append_times) / runs
    comprehension_average = sum(comprehension_times) / runs



    print(f"\nРазмер списка: {size}")
    print("append():", [round(t, 6) for t in append_times])
    print("List comprehension:",
          [round(t, 6) for t in comprehension_times])

    print(f"Среднее append(): {append_average:.6f} сек.")
    print(
        f"Среднее list comprehension: "
        f"{comprehension_average:.6f} сек."
    )