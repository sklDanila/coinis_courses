# Napisati program koji vraća broj cifara u stringu i kreira od njih integer. Primjer: “Hi Mr.
# Rober53. How are you today? Today is 08.10.2019”, štampa 5308102019 i to kao
# integer. Pomoć: da provjerite da li je karakter broj koristiti isdigit metod.


def digit():
    string = input("Enter string: ")
    digits = []

    for i in string:
        if i.isdigit():
            digits.append(i)

    for i in digits:
        print(int(i), end="")


digit()
