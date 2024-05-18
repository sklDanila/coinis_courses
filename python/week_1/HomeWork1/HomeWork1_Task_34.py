# Dobili ste zadatak da generišete specijalni identifikacioni broj za pristup tajnom
# laboratorijskom sektoru. Otkrili ste da se identifikacioni broj može dobiti na
# osnovu poznatog šestocifrenog broja tako što se kvadrira suma cifara tog broja,
# a zatim od tog rezultata oduzme proizvod treće i četvrte cifre istog broja. Kao
# rezultat prikazati identifikacioni broj.

import math


def lab_sector():
    while True:
        num = str(input("Enter six-digit number: "))

        if len(num) == 6:
            sum = 0
            for digit in num:
                sum += int(digit)
            result = pow(sum, 2) - (int(num[2]) * int(num[3]))
            print(f"The special identification number is {result}")
            break
        else:
            print("Enter six-digit number!")


lab_sector()
