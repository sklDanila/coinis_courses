# Dat je četvorocifreni prirodan broj. Napisati kod koji štampa kvadrat zbira cifara
# tog broja.

import math


def sum_digits():
    while True:
        number = str(input("Enter a four-digit number: "))
        sum = 0

        if len(number) == 4:
            for digit in number:
                sum += int(digit)
            print(f"Square of the sum of digits in number {number} is {pow(sum, 2)}")
            break
        else:
            print("The number must be four digits.")


sum_digits()
