# Napisati program koji za unijete vrijednosti a, b, djelilac vraća sumu i broj elemenata
# djeljivih sa djelilac iz segmenta (a, b) (a i b ne pripadaju intervalu)


def divisor():
    a = int(input("Enter the number a: "))
    b = int(input("Enter the number b: "))

    div = int(input("Enter the divisor: "))

    count = 0
    sum = 0

    for i in range(a + 1, b + 1):
        if i % div == 0:
            sum += i
            count += 1
    print(f"Sum = {sum}, Count = {count}")


divisor()
