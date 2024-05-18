# Napisati program koji za 2 data prirodna broja h i o koji redom predstavljaju broj
# molekula vodonika (H) i kiseonika (O), vraća koliko se najviše molekula vode (H2O)
# može dobiti od datih molekula. Npr., ako je h=4, o=3 odgovor je 2.


def task_55():
    h = int(input("Enter number of hydrogen molecules: "))
    o = int(input("Enter number of oxygen molecules: "))

    h2 = h / 2

    if h2 <= o:
        print(
            "The maximum amount of water molecules that can be obtained from these molecules is",
            h2,
        )
    else:
        print("It's impossible to get more than", o, "water molecules")


task_55()
