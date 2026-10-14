import sys

values = [1, 10**100, "", "кот", "к" * 1000]
annotations = ['int', 'long int', 'None', 'str', 'short str', 'long str']

for value, annotate in zip(values, annotations):
    print(annotate, "размер:", sys.getsizeof(value), "байт")
