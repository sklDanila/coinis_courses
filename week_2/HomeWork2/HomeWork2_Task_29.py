# Napisati program koji provjerava da li je uneseni string binarni broj (ima samo 0 ili 1).


def binary():
    while True:
        number = str(input("Enter binary number: "))

        count = 0

        for i in number:
            if i == "0" or i == "1":
                count += 1

        if count == len(number):
            print("Number is binary.")
            break


binary()
