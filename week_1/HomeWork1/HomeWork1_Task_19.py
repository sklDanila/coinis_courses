# Napisati program koji za zadati trocifreni broj računa zbir cifara tog broja.


def sum_number():
    while True:
        number = str(input("Enter a three-digit number: "))

        sum = 0

        if len(number) == 3:
            for num in number:
                sum += int(num)
            print(f"The sum of all numbers is {sum}")
            break
        else:
            print("Enter a THREE-DIGIT number!")


sum_number()
