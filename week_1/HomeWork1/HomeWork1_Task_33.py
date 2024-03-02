# Napisati program koji provjerava koliko se poligona kvadratnog oblika i zadatih
# dimenzija može kreirati na jednoj poljani za koju su poznate njena širina i dužina.


def polygons():
    while True:
        field_width = float(input("Enter a field width: "))
        field_length = float(input("Enter a field length: "))
        polygon_side = float(input("Enter a side length for the square polygon: "))

        if field_length > 0 and polygon_side > 0 and field_width > 0:
            count = (field_length * field_width) / (pow(polygon_side, 2))
            print(f"This number of polygons will fit on field {count}")
            break
        else:
            print("Enter positive numbers!")


polygons()
