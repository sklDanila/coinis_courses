# Napisati program koji sabira sve cifre unijetog broja.


def summ():
    num = str(input("Enter the number: "))

    sum = 0

    for i in num:
        sum += int(i)

    print(f"Sum = {sum}")


summ()
