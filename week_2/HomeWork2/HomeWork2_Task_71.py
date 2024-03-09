# Kreirati program koji analizira zadatu listu brojeva i određuje koliko među njima postoji
# onih brojeva koji nakon primjene kvadratnog korijena zadržavaju svojstvo da budu cijeli
# brojevi. Program treba da prikaže ukupan broj takvih brojeva u listi.
import math


def task_71():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    for i in list:
        new = math.sqrt(i)
        print(new)
        if (new * 10) % 10 == 0:
            count += 1
    print(count)


task_71()
