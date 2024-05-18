# Napisati program kojim se proverava da li se može napraviti bašta u obliku trougla sa
# datim dužinama stranica.


def triangle():
    while True:
        side_a = float(input("Enter side a of the triangle: "))
        side_b = float(input("Enter side b of the triangle: "))
        side_c = float(input("Enter side c of the triangle: "))

        if side_a > 0 and side_b > 0 and side_c > 0:
            if (
                side_a + side_b > side_c
                and side_a + side_c > side_b
                and side_c + side_b > side_a
            ):
                print("The triangle exists")
            else:
                print("The triangle does not exist")
            break
        else:
            print("Invalid input, please enter positive numbers.")


triangle()
