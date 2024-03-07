# Vaš zadatak je da napišete program kojim provjerate da li je strelica pogodila pikado
# tablu. Za pikado tablu je poznat je njegov poluprečnik i koordinate centra, a za strelice
# koordinate cilja.


def target():
    while True:
        x_center_target = int(input("Enter x coordinate for target center: "))
        y_center_target = int(input("Enter y coordinate for target center: "))
        radius_target = int(input("Enter radius for target: "))

        x_arrow = int(input("Enter x coordinate for arrow: "))
        y_arrow = int(input("Enter y coordinate for arrow: "))

        if (
            abs(x_arrow - x_center_target) <= radius_target
            and abs(y_arrow - y_center_target) <= radius_target
        ):
            print("The arrow hit the target.")
            break
        else:
            print("The arrow didn't hit the target. Enter new values.")


target()
