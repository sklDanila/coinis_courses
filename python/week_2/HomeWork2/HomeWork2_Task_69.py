# Napisati program koji umanjujete zarade koje su veće od prosječne za 10 %, a zarade manje od prosječne uvećava za 10 %. Prikazati koliko zarada će biti iznad prosjeka nakon uvećanja/umanjenja.


def task_69():
    list = [1000, 2000, 400, 600]
    avg = sum(list) / len(list)
    print(avg)
    salary = int(input("Enter your salary: "))
    new_salary = 0
    if salary < avg:
        new_salary = salary + salary / 100 * 10
    elif salary > avg:
        new_salary = salary - salary / 100 * 10

    print(f"The new salary is {new_salary - avg} more than the average salary")


task_69()
