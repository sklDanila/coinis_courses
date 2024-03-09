# Napisati program koji vraća zbir kvadrata elemenata liste koji su djeljivi sa 3.


def task_70():
    list = [3, 2, 4, 9, 12]
    sum = 0
    for i in list:
        if i % 3 == 0:
            sum += pow(i, 2)

    return sum


print(task_70())
