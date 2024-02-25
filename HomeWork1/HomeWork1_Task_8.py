# Napisati program kojim se izračunava potrebna dužina trake za ivicu stoljnjaka kružnog
# oblika čija je površina P

import math


def circumference():
    while True:
        square = float(input("Enter square: "))

        if square > 0:
            radius = math.sqrt(square / math.pi)
            tape_length = 2 * math.pi * radius
            print(f"The length of the required tape is {tape_length}")
            break
        else:
            print("Enter a positive square value.")


circumference()
