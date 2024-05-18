# Napisati program za euclide_distance((x1, x2), (y1, y2)) kojom se računa i vraća
# euklidsko rastojanje izmedju dvije tacke A i B. Tacka A par (x1, y1), dok je tačka B par
# (x2, y2).

import math


def euclide_distance():
    x1 = int(input("Enter the x1 coordinate: "))
    x2 = int(input("Enter the x2 coordinate: "))
    y1 = int(input("Enter the y1 coordinate: "))
    y2 = int(input("Enter the y2 coordinate: "))

    distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    print(f"The Euclidean distance between points A and B is {distance}")


euclide_distance()
