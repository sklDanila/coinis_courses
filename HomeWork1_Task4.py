# Sportista se na početku treninga zagrijeva tako što trči po ivicama pravougaonog terena
# dužine d i širine s. Napisati program kojim se određuje koliko metara pretrči sportista dok
# obiđe teren 4 puta.


def runner():
    while True:
        field_length = float(input("Enter length of field: "))
        field_width = float(input("Enter width of field: "))
        if field_length > 0 and field_width > 0:
            distance = (field_length + field_width) * 8
            print(f"The runner will run {distance} meters.")
            break
        else:
            print("Length or width values are negative. Enter positive values.")


runner()
