# Napisati program koji na osnovu dvije varijable start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end) kvadrira sve elemente iz tog segmenta koji
# su djeljivi sa 3 ali ne sa 6, a onda ih sumira. Štampati sumu


def task_60():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    sum = 0

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 6 != 0:
            sum += pow(num, 2)

    print(sum)


task_60()
