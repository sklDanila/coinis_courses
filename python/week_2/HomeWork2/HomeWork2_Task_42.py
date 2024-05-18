# Dat je niz koji sadrži cijene proizvoda u jednom marketu. Market je za ovu nedelju odluči
# da spusti cijene svim proizvodima. Kolika će zarada marketa od tih proizvoda biti manja
# u odnosu na originalnu cijenu.


def task_42():
    lst = [1000, 1000, 1000, 1000, 1000]
    sale = int(input("Enter the sale: "))
    sum = 0

    new_lst = []
    new_sum = 0

    for i in lst:
        new_lst.append(i * sale / 100)
        sum += i

    for i in new_lst:
        new_sum += i

    print("Store revenue will decrease by", sum - new_sum)


task_42()
