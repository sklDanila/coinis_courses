# Dat je četvorocifreni prirodan broj koji predstavlja broj stambene jedinice u
# zgradi. Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi
# stambena jedinica. Poznato je da se to može otkriti iz pretposlednje cifre zadatog
# broja.


def house_floor():
    while True:
        house_number = str(input("Enter house number(four digit number): "))
        if len(house_number) == 4 and int(house_number) > 0:
            floor = int(house_number[-2])
            print(
                f"The apartment is located in building number {house_number} on the {floor}th floor."
            )
            break
        else:
            print("Enter correct house number.")


house_floor()
