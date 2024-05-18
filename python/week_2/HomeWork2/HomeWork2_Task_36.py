# Kreirati program koji unijeti string s (karakteri stringa alfabetski karakteri, mala slova)
# enkriptuje na sledeći način: ako je karakter suglasnik pretvara ga u 0, a ako je karakter
# samoglasnik pretvara ga u 1. Npr. za s = ‘abaae’ rezultat je 10111.


def code():
    string = input("Enter string: ")
    code = []

    for i in string:
        if i.lower() in ["a", "e", "i", "o", "u", "y"]:
            code.append(1)
        else:
            code.append(0)
    for i in code:
        print(int(i), end="")


code()
