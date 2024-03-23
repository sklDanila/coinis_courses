# 3. Data je lista rječnika oblika [{ 'ime': 'Ana', 'godine': 22, 'prosek': 9.1 }, ...]. Napisati funkciju koja
# filtrira studente starije od 21 godine i sortira ih po prosjeku, koristeći filter, sort i lambda funkcije

from functools import reduce


def task_3(list_of_dictionaries):
    filter_age = filter(lambda x: x["godine"] > 21, list_of_dictionaries)
    sort_prosek = sorted(filter_age, key=lambda x: x["prosek"])
    return sort_prosek


list_of_dictionaries = [
    {"ime": "Ana", "godine": 20, "prosek": 9.1},
    {"ime": "Anale", "godine": 23, "prosek": 9.5},
    {"ime": "Anayu", "godine": 25, "prosek": 7.8},
    {"ime": "Anaer", "godine": 24, "prosek": 6.5},
]
print(task_3(list_of_dictionaries))
