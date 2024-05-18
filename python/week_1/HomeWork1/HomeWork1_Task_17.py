# Knjižara "Bukvarnica" je posebno mjesto gdje svaka knjiga ima svoju priču. Kako bi
# proslavili dolazak novog godišnjeg doba, knjižara je odlučila da uvede popust - svaka
# knjiga dobija popust koji se može otkriti samo uz pomoć programa. Kao pomoćnik u
# knjižari, vaš zadatak je da kreirate program koji će izračunati konačnu cijenu knjige
# nakon primijenjenog popusta.


def bookstore():
    while True:
        price = float(input("Enter price for this book: "))
        discount = float(input("Enter the percentage of discount: "))

        # Calculating the final price
        if price > 0 and discount > 0:
            end_price = price - (price / 100 * discount)
            print(f"The final price is {end_price}")
            break
        else:
            print("The price and discount must be positive")


bookstore()
