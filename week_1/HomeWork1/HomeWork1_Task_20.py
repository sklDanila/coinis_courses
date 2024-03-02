# Dobili ste zadatak da dešifrujete kod kojim se otvaraju tajna vrata. Otkrili ste da na
# osnovu poznatog trocifrenog broja možete pronaći kod koji otvara tajna vrata tako što od
# proizvoda cifara tog broja oduzmete zbir cifara istog broja.


def secret_code():
    while True:
        number = str(input("Enter a three-digit number: "))

        sum = 0
        mult = 1

        if len(number) == 3:
            for num in number:
                sum += int(num)
                mult = mult * int(num)
            print(f"The sum of all numbers is {mult - sum}")
            break
        else:
            print("Enter a THREE-DIGIT number!")


secret_code()
