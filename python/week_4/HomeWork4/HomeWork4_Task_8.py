# U fajlu link nalaze se dimenzije pravougaonika (svaki red u fajlu je kombinacija stranica
# pravougaonika a i b, vrijednosti su razdvojene zarezom). Pretpostaviti da se uvijek radi o
# prirodnim brojevima. Vaš zadatak je da iz fajla izdvojite sve pravougaonike koji su kvadrati (a =
# b), i da štampate površinu najvećeg kvadrata. Za ovaj primjer output bi trebao da bude 16
# (kvadrat sa najdužim stranicama je poslednji, čija je dužina stranica 4).

from functools import reduce


def task_8():
    with open("week_4\\class_work\\HomeWork4\\rectangles.txt", "r") as file:
        sides = [tuple(map(int, line.strip().split(","))) for line in file]

    squares = [(a, b) for a, b in sides if a == b]

    max_square = max(squares, key=lambda x: x[0] * x[1])
    max_area = max_square[0] * max_square[1]
    print(max_area)


task_8()
