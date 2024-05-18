# 7. Data je lista ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']. Napisati funkciju koja koristi
# map i reduce da izračuna frekvenciju svakog elementa

from functools import reduce

data = ["apple", "banana", "apple", "orange", "banana", "apple"]


def count_frequency(acc, item):
    if item in acc:
        acc[item] += 1
    else:
        acc[item] = 1
    return acc


pairs = map(lambda x: (x, 1), data)

frequency = reduce(count_frequency, pairs, {})

print(frequency)
