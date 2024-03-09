# Napisati program koji računa zbir najmanje i najveće cifre unesenog broja.


def task_64():
    number = input("Enter number: ")
    zbir = []

    for num in number:
        zbir.append(int(num))

    sum = max(zbir) + min(zbir)
    print(f"The sum of the smallest and largest digits is {sum}")


task_64()
