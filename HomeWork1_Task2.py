# Napisati program koji koristi tri varijable a, b i c, a racuna vrijednosti x1 i x2 kvadratne
# jednacine ax^2 + bx + c = 0. Zanemariti slučaj negativnih vrijednosti ispod korijena
# (kompleksni brojevi).


import math


def quadratic_equation():
    while True:
        a = float(input("Enter coefficient 'a': "))
        b = float(input("Enter coefficient 'b': "))
        c = float(input("Enter coefficient 'c': "))

        D = pow(b, 2) - (4 * c * a)
        if D > 0:
            x1 = ((-b) + math.sqrt(D)) / (2 * a)
            x2 = ((-b) - math.sqrt(D)) / (2 * a)
            print(
                f"The value of x1 from the formula ax^2 + bx + c = 0 is equal to: {x1}, and the value of x2 is equal to: {x2}."
            )
            break
        else:
            print("Enter different values for a, b, and c")


quadratic_equation()
