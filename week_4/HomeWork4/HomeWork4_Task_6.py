# 6. Dat je niz vrijednosti koji predstavlja vremensku seriju. Napisati funkciju koja koristi map da
# izračuna promjenu (diferenciju) između svakog uzastopnog para vrednosti.

from functools import reduce


def task_6(time_series):
    pairs = zip(time_series[:-1], time_series[1:])
    differences = list(map(lambda x: x[1] - x[0], pairs))
    return differences


print(task_6([20, 22, 24, 23, 25, 21, 20]))
