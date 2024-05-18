# Napisati program koji za unijeti string s (provjeriti da li je karakter cifra) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001.


def cipher():
    s = input("Enter string: ")

    mas = []

    for i in s:
        if i.isdigit():
            if int(i) % 2 == 0:
                mas.append(0)
            else:
                mas.append(1)

    for i in mas:
        print(i, end="")


cipher()
