# Napisati program koji obrađuje dvocifreni broj na sledeći način:
# a. Ako je prva cifra veća od druge štampati razliku prve i druge cifre
# b. Ako je prva cifra manja od druge štampati zbir te dvije cifre
# c. Ako su cifre iste štampati njihov proizvod


def two_digit():
    while True:
        number = str(input("Enter two-digit number: "))
        if len(number) == 2:
            if int(number[0]) > int(number[1]):
                print(
                    f"difference between first and second digit = {int(number[0])-int(number[1])}"
                )

            elif int(number[0]) < int(number[1]):
                print(f"sum of the digits = {int(number[0])+int(number[1])}")
            else:
                print(f"product of the digits = {int(number[0])*int(number[1])}")
            break
        else:
            print("Please enter a two-digit number.")


two_digit()
