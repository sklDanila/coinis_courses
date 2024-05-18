# Napisati program koji za unijete parametre a i b vraća srednju vrijednost.
# Npr. ako je a = 2, b = 3, rezultat funkcije treba da bude 2.5. Ako je a = -2, b = 4,
# rezultat treba da bude 1. Ako je a = -4, b = 2, rezultat treba da bude - 1.


def average_value(a, b):
    average = (a + b) / 2
    print(f"Average value of variables a and b: {average}")


average_value(int(input("Enter value a: ")), int(input("Enter value b: ")))
