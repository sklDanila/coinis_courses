# Dato je rastojanje u centimetrima između ulaza u dvije različite kancelarije.
# Odrediti koliko cijelih metara ima u tom rastojanju. Npr. 324cm imaju 3 metra.


def distance():
    distance_cen = int(input("Enter the distance between the doors in centimeters: "))

    distance_m = distance_cen // 100
    print(f"Distance {distance_cen} in centimeters = distance {distance_m} in meters")


distance()
