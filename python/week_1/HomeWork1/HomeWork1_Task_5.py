# Napisati program koji na osnovu zadate širine i visine lista papira (pravougaonog oblika)
# u milimetrima određuje njegovu površinu u kvadratnim centimetrima.


def paper():
    while True:
        width = float(input("Enter the width of the paper in millimeters: "))
        length = float(input("Enter the width of the paper in millimeters: "))

        if length > 0 and width > 0:
            print(
                f"The area of the sheet is equal to {(width * length) / 100} centimeters"
            )
            break
        else:
            print("Enter positive length and width values")


paper()
