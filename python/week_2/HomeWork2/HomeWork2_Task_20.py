# Napisati program koji računa zbir parnih cifara ukoliko je broj paran, a ukoliko je neparan
# proizvod neparnih cifara četvorocifrenog broja. Broj n unosi korisnik.


def number():
    while True:
        num = str(input("Enter four-digit number: "))

        sum = 0
        mult = 1

        if len(num) == 4:
            if int(num) % 2 == 0:
                for i in num:
                    if int(i) % 2 == 0:
                        sum += int(i)
                print(f"The sum of even numbers is {sum}")
            else:
                for i in num:
                    if int(i) % 2 != 0:
                        mult *= int(i)
                print(f"The product of odd numbers is {mult}")
            break
        else:
            print("Enter a four-digit number!")


number()
