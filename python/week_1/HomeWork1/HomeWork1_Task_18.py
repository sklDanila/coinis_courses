# Cijena konzole za igre PlayStation 5 je prvo porasla 10%, pa je smanjena 10%. Ako je
# poznata početna cijena konzole, napisati program koji određuje cijenu nakon tih
# promjena


def PlayStation():
    while True:
        price = float(input("Enter the price of PlayStation: "))

        if price > 0:
            price_up = price + (price * 0.1)
            price_down = price_up - (price_up * 0.1)
            print(f"Price after discount is {price_down}")
            break
        else:
            print("Enter positive price")


PlayStation()
