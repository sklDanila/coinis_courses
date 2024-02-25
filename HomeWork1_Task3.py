# Napisati program koji racuna razliku kvadrata


def difference_of_squares(number1, number2):
    print(f"Difference of squares: {(number1 - number2) * (number1 + number2)}")


difference_of_squares(
    int(input("Enter the first number: ")), int(input("Enter the second number: "))
)
