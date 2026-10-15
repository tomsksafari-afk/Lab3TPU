import sys

N = 1000
d = {i: f"value_{i}" for i in range(N)}
lst = list(zip(range(N), [f"value_{i}" for i in range(N)]))
tpl = tuple(zip(range(N), [f"value_{i}" for i in range(N)]))
s = set(zip(range(N), [f"value_{i}" for i in range(N)]))
print(f'd={sys.getsizeof(d)} байт, lst={sys.getsizeof(lst)} байт, tpl={sys.getsizeof(tpl)} байт, s={sys.getsizeof(s)} байт')
print(d[10])
