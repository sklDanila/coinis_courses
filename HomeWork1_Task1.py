# Napisati program koji racuna površinu i obim pravougaonika


def area_perimeter_rectangle(side_a, side_b):
    area = side_a * side_b
    print(f"Area of rectangle: {area}")
    perimeter = (side_a + side_b) * 2
    print(f"Perimeter of rectangle: {perimeter}")


area_perimeter_rectangle(
    int(input("Enter the length of the first side: ")),
    int(input("Enter the length of the second side: ")),
)
