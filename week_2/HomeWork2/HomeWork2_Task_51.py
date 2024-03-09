# Lozinka je jaka ako je njena dužina najmanje 8 simbola, i sadrži mala slova, velika slova
# i cifre. Napisati program koji provjerava da li je lozinka jaka. Ulaz: Unosi se jedna riječ,
# dužine ne veće od 100, koja sadrži mala i velika slova i cifre. Izlaz: Štampati YES ili NO.
def task_51():
    while True:
        password = input("Enter your password: ")

        if len(password) >= 8 and len(password) <= 100:
            count_lower = 0
            count_digit = 0
            count_upper = 0
            for i in password:
                if i.islower():
                    count_lower += 1
                elif i.isdigit():
                    count_digit += 1
                elif i.isupper():
                    count_upper += 1
            if count_lower > 0 and count_digit > 0 and count_upper > 0:
                print(count_lower, count_digit, count_upper)
                print("YES")
                break
            else:
                print("NO")
        else:
            print("Enter password lenght by 8 to 100")


task_51()
