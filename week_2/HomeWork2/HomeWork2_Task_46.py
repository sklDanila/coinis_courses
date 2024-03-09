# Kreirati program koji nalazi platu zaposlenog koji ima drugo najveće primanje. Npr. ako
# je plate = [540,690, 900] rezultat je 690. Napomena: lista ima bar 2 elementa.


def task_46():
    salaries = [540, 690, 900]
    salaries.sort()
    second_max_salary = salaries[1]

    print(second_max_salary)


task_46()
