# Napisati program koji racuna kvadrat trinoma(a, b, c) koja za unijete parametre a, b i c
# računa kvadrat trinoma za unešene parametre. Formula: 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 +
# 2𝑏c

import math


def square_of_trinomial(a, b, c):
    result = pow(a, 2) + pow(b, 2) + pow(c, 2) + 2 * a * b + 2 * a * c + 2 * b * c
    print(
        f"The result of calculating a quadratic trinomial based on 3 parameters is {result}"
    )


square_of_trinomial(
    int(input("Enter parameter a: ")),
    int(input("Enter parameter b: ")),
    int(input("Enter parameter c: ")),
)
