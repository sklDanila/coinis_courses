# Napisati program koji računa zbir parnih i proizvod neparnih brojeva od 1 do n. Broj n
# unosi korisnik.
# a. Štampati taj zbir i proizvod.
# b. Štampati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta


def calculate():
    n = int(input("Enter last number n: "))

    sum = 0
    count_even = 0
    mult = 1
    count_odd = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
            count_even += 1
        else:
            mult *= i
            count_odd += 1

    print(
        f"Sum of even numbers is {sum}, product of odd is {mult}.\nCount of even numbers is {count_even}.\nCount of odd numbers is {count_odd}."
    )


calculate()
