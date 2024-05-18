# Napisati Python funkciju kojom tražite najduži testerasti podniz. Testerasti podniz je onaj za koji
# važi da je prvi broj manji od drugog, drugi da je veći od trećeg, treći manji od četvrtog, itd.


def task_3():
    list = [1, 2, 3, 2, 1, 5, 4, 3, 2, 1]
    max_lenght = 0
    lenght = 1
    result = []

    for i in range(len(list) - 1):
        if (i % 2 == 0 and list[i] < list[i + 1]) or (
            i % 2 == 1 and list[i] > list[i + 1]
        ):
            lenght += 1
        else:
            if lenght > max_lenght:
                max_lenght = lenght
                result = list[i - lenght + 1 : i + 1]
            lenght = 1

    if lenght > max_lenght:
        result = list[len(list) - lenght :]

    print(result)


task_3()
