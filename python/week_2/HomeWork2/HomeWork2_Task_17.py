# Napisati program koji provjerava da li se od pravouganika poznatih dimenzija stranica
# mogu napraviti bar dva kvadrata čija je duzina ista kao i dužina pravouganika.


def rectangle():
    rectangle_lenght = int(input("Enter rectangle lenght: "))
    rectangle_width = int(input("Enter rectangle width: "))

    if rectangle_lenght / rectangle_width == 2:
        print(
            "it is possible to create at least two squares with the same length from a rectangle with known side dimensions"
        )
    else:
        print("You cant")


rectangle()
