#  Napisati program koji provjerava koliko se određeni broj ponavlja u listi (taj broj unosi
# korisnik).


def task_67():
    list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 2]
    number = int(input("Enter number: "))
    count = 0
    for i in list:
        if i == number:
            count += 1
    print(count)


task_67()
