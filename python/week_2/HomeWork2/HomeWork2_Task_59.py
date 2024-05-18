# Napisati program koji za unijeti string s (karakteri stringa cifre od 0 do 9) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001. Pomoć: Inicijalna vrijednost za
# dodatni string je “”, a onda se pomoću operatora + nadodaje 0 ili 1 u zavisnosti u
# ispunjenosti uslova.


def task_59():
    s = input("Enter string: ")
    new_s = ""

    for i in s:
        if i.isdigit():
            if int(i) % 2 == 0:
                new_s += "0"
            else:
                new_s += "1"

    print(new_s)


task_59()
