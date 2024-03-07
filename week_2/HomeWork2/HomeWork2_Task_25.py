# Napisati program kojim se uklanja prvi i poslednji karakter teksta i štampa novi tekst


def delete():
    text = str(input("Enter text: "))
    text = text[1:-1]
    print(text)


delete()
