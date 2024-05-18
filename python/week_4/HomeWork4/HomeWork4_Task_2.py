# 2. Date su dvije liste, jedna sa imenima studenata, a druga sa njihovim prosječnim ocjenama.
# Napisati funkciju koja pronalazi studente sa prosječnom ocjenom iznad 8.5 i vraća listu torki (ime,
# ocjena) za te studente.

from functools import reduce


def task_2(list_names, list_grades):
    best_grades = filter(lambda x: x[1] > 8.5, zip(list_names, list_grades))
    return list(best_grades)


list_names = ["Danila", "Ruslan", "Balsa", "Elena"]
list_grades = [4.6, 5.3, 8.6, 9.3]
result_list = task_2(list_names, list_grades)
print(result_list)
