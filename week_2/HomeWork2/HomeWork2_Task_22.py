# Za unijetu tačku sa koordinata (x,y) provjeriti kom kvadratnu pripada u koordinatnom
# sistemu.


def quadrants():
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))

    if x > 0 and y > 0:
        print("First quadrant")
    elif x < 0 and y > 0:
        print("Second quadrant")
    elif x < 0 and y < 0:
        print("Third quadrant")
    elif x > 0 and y < 0:
        print("Fourth quadrant")


quadrants()
