# Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e, napisati kod koji za
# unijeti broj pređenih kilometara računa cijenu vožnje.


def taxi():
    while True:
        km = float(input("Enter the number of kilometers driven: "))
        if km > 0:
            payment = 1 + (km * 0.5)
            print(f"You need to pay {payment} euros.")
            break
        else:
            print("Please enter positive number of killometars.")


taxi()
