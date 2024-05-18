# Vaš zadatak je da napišete program kojim ćete provjeriti da li se mrav kreće po ivici
# stola. Geometrijski, mrav se predstavlja kao tačka, a za sto su poznate tjemena desne
# gornje i lijeve donje ivice stola. Radi jednostavnosti smatrati da je sto pravouganik, ne
# kvadar.


def ant():
    x_top_right = int(
        input("Enter x coordinate for the top right corner of the rectangle: ")
    )
    y_top_right = int(
        input("Enter y coordinate for the top right corner of the rectangle: ")
    )
    x_bottom_left = int(
        input("Enter x coordinate for the bottom left corner of the rectangle: ")
    )
    y_bottom_left = int(
        input("Enter y coordinate for the bottom left corner of the rectangle: ")
    )

    x_ant = int(input("Enter x coordinate for the position of the ant on the table: "))
    y_ant = int(input("Enter y coordinate for the position of the ant on the table: "))

    if x_bottom_left <= x_ant <= x_top_right and y_bottom_left <= y_ant <= y_top_right:
        print("Ant walks along the edge.")
    else:
        print("Ant dont walk along the edge.")


ant()
