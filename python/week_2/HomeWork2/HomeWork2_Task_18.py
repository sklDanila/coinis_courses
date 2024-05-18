# Napisati program kojim se na osnovu temperature vode određuje njeno agregatno
# stanje. Ako je temperatura:
# • viša od 0 C i niža od 100C - agregatno stanje je tečno
# • ne viša od 0 C - agregatno stanje je čvrsto,
# • ne niža od 100 C - agregatno stanje je gasovito.
# Za temperaturu od tačno 0 smatra se da je agregatno stanje čvrsto, a za tačno 100 da je
# gasovito.
# Ulaz: Temperatura - cio broj
# Izlaz: Na standardni izlaz ispisati jednu od sledećih riječi: cvrsto, tecno, gasovito.


def temperature():
    temperature = int(input("Enter temperature in Celsius: "))

    if 0 < temperature < 100:
        print("liquid")
    elif temperature < 0 or temperature == 0:
        print("hard")
    elif temperature > 100 or temperature == 100:
        print("gaseous")


temperature()
