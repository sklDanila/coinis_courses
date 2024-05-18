# Kreirati program koji prikazuje koliko ima zaposlenih koji imaju veće plate od prosječne
# plata. Npr. ako su plate = [500, 600, 700] rezultat je 1 jer je samo plata od 700 EUR
# iznad prosječne plate.


def task_45():
    salaries = [500, 600, 700]
    average_salary = sum(salaries) / len(salaries)

    count = 0
    for s in salaries:
        if s > average_salary:
            count += 1

    print(count)


task_45()
