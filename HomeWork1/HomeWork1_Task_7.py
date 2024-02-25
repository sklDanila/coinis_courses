# Marko voli biciklizam. Pošto Marko zna da je važno biti hidratizovan, pije vodu na svakih
# sat vremena vožnje bicikla i to pola litara vode. Kao ulaz poznato je vrijeme u satima, a
# treba štampati broj litara koje će Marko popiti, zaokruženo na najmanju vrijednost (donje
# cijelo).
# Primjer: time = 3 ----> litara = 1; time = 6.7---> litara = 3 ; time = 11.8--> litara = 5

import math


def water():
    while True:
        distance = float(input("Enter distance: "))

        if distance > 0:
            water_volume = math.trunc(distance * 0.5)
            print(f"The cyclist drank {water_volume} liters of water")
            break
        else:
            print("Enter a positive distance value.")


water()
