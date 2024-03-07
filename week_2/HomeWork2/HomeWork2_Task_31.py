# Napisati program sa dva ulaza (korisnik unosi) start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end), a koja kvadrira sve elemente iz tog
# segmenta koji su djeljivi sa 2 ali ne sa 4, a onda ih sumira. Štampati sumu


def sum():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    sum = 0

    for num in range(start, end + 1):
        if num % 2 == 0 and num % 4 != 0:
            sum += pow(num, 2)

    print(sum)


sum()
