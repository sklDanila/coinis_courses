# Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.


def replacement():
    while True:
        number = str(input("Enter a three-digit number: "))

        mas = []

        if len(number) == 3:
            for digit in number:
                mas.append(int(digit))
            print(f"New number is {mas[-1]}{mas[1]}{mas[0]}")
            break
        else:
            print("Invalid number! Please, enter a three-digit number.")


replacement()
