# Napisati program koji uvećava zarade koje su veće od prosječne zarade (prosjek liste)
# za X eura.


def task_68():
    list = [1000, 500, 600, 100, 700, 1200]
    X = int(input("Enter the value of upper salary: "))

    avg_list = sum(list) / len(list)

    new_salary = avg_list + X
    print(new_salary)


task_68()
