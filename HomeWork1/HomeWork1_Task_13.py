# Zamislite da ste dobili tajanstveno pismo sa mapom i uputstvima za pronalaženje
# skrivenog blaga. Uputstva su sljedeća: "Trebate da krenete od starog hrasta koji ima
# sledeću poziciju G (x1,y1). Onda trebate ići pravo do stare kuće koja se nalazi na poziciji
# K(x2,y2). Blago je zakopano u susjedstvu, gdje se nalazi kuća, i to desno od pozicije
# kuće za dvije pozicije, i ispod za tri pozicije.
# a. Izračunajte koordinate blaga.
# b. Izračunajte (vazdušno) rastojanje od hrasta do blaga.
# c. Izračunajte rastojanje od hrasta do blaga tako da morate obići i kuću.

import math


def hidden_treasures():
    x1 = int(input("Enter coordinate x1 for the old tree: "))
    y1 = int(input("Enter coordinate y1 for the old tree: "))
    x2 = int(input("Enter coordinate x2 for the house: "))
    y2 = int(input("Enter coordinate y2 for the house: "))

    x_treasures = x2 + 2
    y_treasures = y2 - 3
    print(f"Coordinates of treasures - ({x_treasures}, {y_treasures})")

    treeToTreasures = math.sqrt(pow((x_treasures - x1), 2) + pow((y_treasures - y1), 2))
    print(f"The distance from the oak tree to the treasure is {treeToTreasures}")

    treeToHouse = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    houseToTreasures = math.sqrt(
        pow((x_treasures - x2), 2) + pow((y_treasures - y2), 2)
    )
    treeToHouseToTreasures = treeToHouse + houseToTreasures
    print(
        f"The distance from the oak to the treasure through the house is {treeToHouseToTreasures}"
    )


hidden_treasures()
