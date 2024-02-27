# Napiši program koji izračunava površinu trougla ako su poznate koordinate njegovih
# tjemena. (pomoc: Heronov obrazac i euklidsko rastojanje)

import math


def area_triangle():
    x1 = int(input("Enter the coordinates of the x1: "))
    y1 = int(input("Enter the coordinates of the y1: "))
    x2 = int(input("Enter the coordinates of the x2: "))
    y2 = int(input("Enter the coordinates of the y2: "))
    x3 = int(input("Enter the coordinates of the x3: "))
    y3 = int(input("Enter the coordinates of the y3: "))

    side_a = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    side_b = math.sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2))
    side_c = math.sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2))

    p = (side_a + side_b + side_c) / 2

    area = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

    print(f"Area of triangle is {area}")


area_triangle()
