# Napisati program koji za unijetu listu L i vrijednost max vraća broj elemenata koji su
# manji od max iz te liste. Napomena: lista sadrži samo cijele brojeve
# Input: a = [1,2,3], max = 3; Output: 2
# Input: a = [-1, 0, 5], max = -2; Output: 0


def task_41():
    maas = []
    num = input("Enter number(if you want to exit enter exit): ")
    while num != "exit":
        maas.append(num)
        num = input("Enter number(if you want  to exit enter exit): ")
    max = int(input("Enter max value: "))

    count = 0

    for i in maas:
        if int(i) < max:
            count += 1
    print(count)


task_41()
