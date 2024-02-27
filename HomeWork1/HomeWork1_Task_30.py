# Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće
# izrezati iz tog pravougaonika?


import math


def squares():
    sideA_rectangle = 543
    sideB_rectangle = 130

    side_square = 65

    countOfSquares = (sideA_rectangle * sideB_rectangle) / pow(side_square, 2)

    print(f"This number of squares can be cut from a rectangle - {countOfSquares}")


squares()
