# Vaš zadatak je da napravite program kojim provjeravate da li se pčela kreće po žici. Žica
# se može predstaviti pravom y = 2 * x + 5, dok se pčela predstavlja tačkom (x, y).


def bee():
    while True:
        x = int(input("Enter x coordinate of the bee: "))
        y = int(input("Enter y coordinate of the bee: "))

        if y == ((2 * x) + 5):
            print("Bee moves along the line")
        else:
            print("Bee dont move along the line")
        break


bee()
