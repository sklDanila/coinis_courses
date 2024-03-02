# Dat je šestocifreni broj n (n=abcdef). Provjeriti da li važi a* c + 2 + f = b + d*e.
# Pomoć: razmisliti o provjeri uslova (boolean operator) - samostalno isprobati
# implementaciju iste u Python-u. Ovo ćemo svakako raditi tokom naredne
# sedmice.


def six_digit():
    while True:
        num = str(input("Enter a six-digit number: "))

        if len(num) == 6:
            print(
                int(num[0]) * int(num[2]) + 2 + int(num[5])
                == int(num[1]) + int(num[3]) * int(num[4])
            )
            break
        else:
            print("Enter six-digit number!")


six_digit()
