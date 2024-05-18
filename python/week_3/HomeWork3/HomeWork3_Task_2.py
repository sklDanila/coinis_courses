# Napisati program koji nalazi ponavljajuću sekvencu (podniz) koja u proizvodu daje najveću
# vrijednost. Štampati tu sekvencu i proizvod te sekvence. Primjer: za listu [1, 2, 2, 2, 4, 4] treba da
# se štampa sekvenca [4, 4] i proizvod 16.


# def task_2():
#     numbers = [1, 2, 2, 2, 4, 4]
#     sup = 1
#     suo = 1
#     mas = []
#     for i in numbers:
#         for j in numbers:
#             if j == i:
#                 mas.append(j)
#         for j in mas:
#             sup *= j
#         if sup > suo:
#             suo = sup
#         print(mas)
#         print(f"Proizvod = {sup}")
#         sup = 1
#         mas = []


# task_2()


def task_2():
    numbers = [1, 2, 2, 2, 4, 4]
    result_mas = []
    result_sup = 1
    now_mas = []
    now_sup = 1

    for num in numbers:
        if now_mas and num == now_mas[-1]:
            now_mas.append(num)
            now_sup *= num
        else:
            now_mas = [num]
            now_sup = num
        if now_sup > result_sup:
            result_sup = now_sup
            result_mas = now_mas.copy()

    print(result_mas)
    print(result_sup)


task_2()
