# Lista se sastoji od ocjena studenata na predmetu Ekonomija i razvoj. Koliko studenata je
# dobilo veću ocjenu od prosječne ocjene (ocjena 5 ne utiče na prosjek)


def task_72():
    grades = [5, 6, 7, 8, 9, 10, 9, 7, 7, 8]
    sum = 0
    count_grades = 0
    for i in grades:
        if i > 5:
            sum += i
            count_grades += 1
    avg = sum / count_grades
    print(avg)
    count = 0
    for i in grades:
        if i > avg:
            count += 1

    print(count)


task_72()
