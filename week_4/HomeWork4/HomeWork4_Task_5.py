# 5. Data je lista torki oblika [(ime, ocjena, predmet), ...]. Napisati funkciju koja koristi filter, map, i
# reduce da izračuna prosječnu ocjenu po predmetu

from functools import reduce


def task_5(list_of_tuples, subject):
    filter_list_of_tuples = filter(lambda x: x[2] == subject, list_of_tuples)
    filter_list_of_tuples = list(filter_list_of_tuples)
    sum_ocjene = reduce(lambda acc, el: acc + el[1], filter_list_of_tuples, 0)
    broj_ocjena = len(filter_list_of_tuples)
    return sum_ocjene / broj_ocjena if broj_ocjena != 0 else None


print(
    task_5(
        [
            ("Danila", 5, "mathematics"),
            ("Pavel", 5, "english"),
            ("Stefan", 4, "mathematics"),
        ],
        "mathematics",
    )
)
