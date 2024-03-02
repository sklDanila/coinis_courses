# Otkrili ste algoritam kojim možete doći do šifre koja otvara sef. U sefu se nalazi knjiga
# koja krije tajne o nastanku univerzuma. Šifra se dobija kada se od kvadrata zbira prve i
# poslednje cifre četvorocifrenog broja oduzme razlika kvadrata druge i trece cifre.

import math


def seif():
    while True:
        number = str(input("Enter a four-digit number: "))

        if len(number) == 4:
            result = (pow((int(number[0]) + int(number[-1])), 2)) - (
                pow(int(number[1]), 2) - pow(int(number[2]), 2)
            )
            print(f"Code for open seif is {result}")
            break
        else:
            print("Enter a FOUR-DIGIT number!")


seif()
