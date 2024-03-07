# Za dva stola kružnog oblika poznat je njihov poluprečnik. Napisati kod kojim se štampa
# obim stola sa većom površinom.

import math


def tables():
    table1_radius = int(input("Enter radius for first table: "))
    table2_radius = int(input("Enter radius for second table: "))

    table1_area = math.pi * pow(table1_radius, 2)
    table2_area = math.pi * pow(table2_radius, 2)

    if table1_area > table2_area:
        print(
            f"The larger area is of the first table and its perimeter is {2 * math.pi * table1_radius}."
        )
    elif table1_area < table2_area:
        print(
            f"The larger area is of the second table and its perimeter is {2 * math.pi * table2_radius}."
        )


tables()
