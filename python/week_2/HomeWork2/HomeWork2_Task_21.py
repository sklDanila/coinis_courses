# Napisati program koji za zadato x računa y i to na sledeći način

import math


def function():
    x = int(input("Enter the x: "))

    if x <= -7:
        y = -2 * x + 7 / 2
        print(f"y = {y}")
    elif -7 < x < 1:
        y = (pow(x, 2) - (3 * x) + 5) / (pow(x, 2) + 2)
        print(f"y = {y}")
    elif 1 <= x <= 8:
        y = (math.sqrt(pow(x, 2) + 2 * x + 2)) + (math.sqrt(abs((3 / 2 * x) - (4 / 7))))
        print(f"y = {y}")
    elif x > 8:
        y = abs((3 / pow(x, 2)) - (11 * x))
        print(f"y = {y}")


function()
