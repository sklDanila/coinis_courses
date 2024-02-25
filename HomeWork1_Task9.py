# Fudbalski teren dimenzija d×s treba ograditi pravougaonom ogradom tako da je
# rastojanje stranica ograde od linije terena r. Napiši program koji određuje dužinu ograde.
# Ulaz: U tri reda standardnog ulaza nalaze se tri cijela broja:
# • d - dužina terena u metrima
# • s - širina terena u metrima
# • r - rastojanje ograde od terena u metrima
# Izlaz: Duzina ograde u metrima


def fence_length():
    while True:
        field_width = float(input("Enter width of  the football field in meters: "))
        field_length = float(input("Enter length of the football field in meters: "))
        distance_from_field = float(
            input("Enter the distance from the field to the fence in meters: ")
        )

        if field_width > 0 and field_length > 0 and distance_from_field > 0:
            fence_length = (
                (field_length + (distance_from_field * 2))
                + ((field_width + (distance_from_field * 2)))
            ) * 2
            print(f"The length of the fence around the field is {fence_length}")
            break
        else:
            print("One of the values you entered is invalid.")


fence_length()
