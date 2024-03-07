# Napisati program kojim se provjerava da li se tačka nalazi unutar pravouganika. Za
# pravougaonik su date koordinate gornjeg lijevog i donjeg desnog tjemena.


def point():
    rectangle_top_left_x = int(input("Enter rectangle top left x coordinate: "))
    rectangle_top_left_y = int(input("Enter rectangle top left y coordinate: "))
    rectangle_bottom_right_x = int(input("Enter rectangle bottom right x coordinate: "))
    rectangle_bottom_right_y = int(input("Enter rectangle bottom right y coordinate: "))

    point_x = int(input("Enter point x coordinate: "))
    point_y = int(input("Enter point y coordinate: "))

    if (
        rectangle_bottom_right_x > point_x > rectangle_top_left_x
        and rectangle_bottom_right_y < point_y < rectangle_top_left_y
    ):
        print("Point in rectangle")
    else:
        print("Point out of rectangle")


point()
