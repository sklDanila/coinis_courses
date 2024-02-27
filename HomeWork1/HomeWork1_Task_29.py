# Korisnik unosi koordinate dvije tačke (x1, y1) i (x2, y2) koje predstavljaju početne
# tačke dva studenta koji su se dogovorili da se sretnu na lokaciji (x3, y3) koja je
# nalazi tačno na sredini njihovog puta. Program treba da odredi tu lokaciju i
# izračuna rastojanje od početne pozicije do tačke susreta, koristeći Euklidsko
# rastojanje.

import math


def students():
    x1 = float(input("Enter student x1 coordinate: "))
    y1 = float(input("Enter student y1 coordinate: "))
    x2 = float(input("Enter student x2 coordinate: "))
    y2 = float(input("Enter student y2 coordinate: "))

    distance_students = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    print(f"The distance to the meeting point is {distance_students/2}")


students()
