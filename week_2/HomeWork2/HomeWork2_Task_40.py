# Napisati program koji na osnovu niza cijelih brojeva računa apsolutnu sumu svih
# negativnih parnih elemenata za unijeti niz. Štampati sumu.
# Primjer:
# Input: [-2, 7, -5, 3, 1, -4]
# Output: 6 (|-2| + |-4|)


def task_40():
    maas = []
    num = input("Enter number(if you want to exit enter exit): ")
    while num != "exit":
        maas.append(num)
        num = input("Enter number(if you want  to exit enter exit): ")
    sum = 0
    for i in maas:
        if int(i) < 0 and int(i) % 2 == 0:
            sum += abs(int(i))
    print(sum)


task_40()
