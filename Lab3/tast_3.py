import timeit

for n in [1_000, 10_000, 100_000]:
    data_list = list(range(n))
    data_set = set(range(n))
    target_found = n // 2
    target_missing = n + 999999

    t_list = timeit.timeit("target in coll", globals={"coll": data_list, "target": target_found}, number=1000)
    t_set  = timeit.timeit("target in coll", globals={"coll": data_set,  "target": target_found}, number=1000)
    t_list_missing = timeit.timeit("target in coll", globals={"coll": data_list, "target": target_missing}, number=1000)
    t_set_missing  = timeit.timeit("target in coll", globals={"coll": data_set,  "target": target_missing}, number=1000)

    print(f"n={n}: list found={t_list:.6f}, set found={t_set:.6f}, list missing={t_list_missing:.6f}, set missing={t_set_missing:.6f}")
