# Date su koordinate donje desne i gornje lijeve ivice zida (pravougaonik). Izračunati
# povrsinu i obim zida.


def wall_perimeter_area():
    upper_left_x = int(input("Enter the x coordinate of the top left corner: "))
    upper_left_y = int(input("Enter the y coordinate of the top left corner: "))
    lower_right_x = int(input("Enter the x coordinate of the lower right corner: "))
    lower_right_y = int(input("Enter the y coordinate of the lower right corner: "))

    bottom_side_length = lower_right_x - upper_left_x
    side_length = upper_left_y - lower_right_y

    wall_area = bottom_side_length * side_length
    wall_perimeter = (bottom_side_length + side_length) * 2

    print(f"The area of the wall is {wall_area} and the perimeter is {wall_perimeter}")


wall_perimeter_area()
