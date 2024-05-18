# Data je lista koja se sastoji od cijelih brojeva. Provjeriti da li u listi ima više dvocifrenih ili
# trocifrenih brojeva.


def task_66():
    list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 456, 768, 687]

    count_two = 0
    count_three = 0

    for i in list:
        if len(str(i)) == 2:
            count_two += 1
        elif len(str(i)) == 3:
            count_three += 1
    if count_two > count_three:
        print("Two-digit numbers more")
    elif count_three > count_two:
        print("Three-degit numbers more")


task_66()
