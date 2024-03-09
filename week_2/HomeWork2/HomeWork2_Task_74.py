# Napisati program koji za zadatu listu plata zaposlenih u jednoj IT kompaniji (plate se
# unose u eurima) računa prosječnu vrijednost plata u dolarima ako je poznato da je 1e =
# 1.1$


def task_74():
    salaries = [1000, 2000, 2500, 5000, 1500]
    avg = sum(salaries) / len(salaries)
    dollars = avg * 1.1
    print(dollars)


task_74()
