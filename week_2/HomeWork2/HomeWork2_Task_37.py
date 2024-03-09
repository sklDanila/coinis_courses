# Igrač nasumično bira listicu na kojoj se nalazi tekst sastavljen od karaktera 1, 0 i *.
# Karakter 1 nosi 1 poen, 0 nosi 0 poena, dok * nosi -1 poen. Napisati program koji
# provjerava da li je igrač u plusu.


def gamer():
    card = input("Enter value of card: ")

    if card == "1":
        print("The player is in the black")
    else:
        print("The player is in the red")


gamer()
