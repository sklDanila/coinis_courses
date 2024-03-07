# Date su cijene tri proizvoda. Naći par proizvoda čija cijena u zbiru daje najmanju
# vrijednost.


def prices():
    product1_price = float(input("Enter price for the first product: "))
    product2_price = float(input("Enter price for the second product: "))
    product3_price = float(input("Enter price for the third product: "))

    sum = product1_price + product2_price

    if product1_price + product3_price < sum:
        print("The cheapest combination is first and third products.")
    elif product2_price + product3_price < sum:
        print("The cheapest combination is second and third products.")
    else:
        print("The cheapest combination is first and second products.")


prices()
