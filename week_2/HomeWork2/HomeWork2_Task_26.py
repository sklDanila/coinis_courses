# Napisati program koji provjerava da li je korsnik unio binarni, oktalni, dekadni ili
# heksadecimalni broj. Binarni broj ima prefiks 0b, oktalni 0o, heksadecimalni 0x, a
# dekadni nema prefiks.


def prefiks():
    num = str(input("Enter number: "))

    if num[0:2] == "0b":
        print("Binary number")
    elif num[0:2] == "0o":
        print("Octal number")
    elif num[0:2] == "0x":
        print("hexadecimal number")
    else:
        print("decimal number")


prefiks()
