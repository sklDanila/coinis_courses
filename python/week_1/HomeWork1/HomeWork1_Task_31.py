# Napisati program koji računa površinu ekrana monitora pravougaonog oblika,
# ukoliko je poznata dužina njegove dijagonale (d = 50) i odnos stranica (aspect
# ratio = 16:9).

import math


def area():
    d = 50
    side1_ratio = 16
    side2_ratio = 9

    x = math.sqrt(pow(d, 2) / (pow(side1_ratio, 2) + pow(side2_ratio, 2)))

    side1 = x * side1_ratio
    side2 = x * side2_ratio

    screen_area = side1 * side2
    print(f"Screen area is {screen_area}")


area()
