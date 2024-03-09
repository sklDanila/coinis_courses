# Napisati program koji iz teksta izvlači cifre i računa njihov proizvod.


def product():
    text = input("Enter the text: ")

    prod = 1

    for i in text:
        if i.isdigit():
            prod *= int(i)

    print(f"Product is {prod}")


product()
