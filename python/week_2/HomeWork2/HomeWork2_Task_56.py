# Napisati program kojim za unijeti string provjeravate koliko ima jednocifrenih negativnih
# brojeva. String se sastoji od negativnih i pozitivnih brojeva i oznaka za negativne (-) i
# pozitivne (+). Primjer: +23-2-32+4-22-4 izlaz je 2.


import re


def task_56():
    string = input("Enter the string: ")
    splited_string = re.split("(?=[-+])", string)
    count = 0
    for i in splited_string:
        if i.startswith("-"):
            if len(i) == 2:
                count += 1

    print(count)


task_56()
