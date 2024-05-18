# Napisati program koji za unijeti string a prebrojava koliko ima heksadecimalnih brojeva.
# Broj je heksadecimalni ako ima prefiks 0x. Svaki broj je razdvojena razmakom (space)
# Ulaz 1: a = “12 0x1A 0001 121 0x2”; Izlaz 1: 2
# Ulaz 2: a = “12 001 31”; Izlaz 2: 0


def task_62():
    a = input("Enter the string: ")
    new_a = a.split(" ")
    count = 0

    for i in new_a:
        if i[:2] == "0x":
            count += 1

    print(count)


task_62()
