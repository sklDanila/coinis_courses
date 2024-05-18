# Napisati program koji vraća velika slova iz zadatog unijetog teksta kao jedan novi string.
# Ulaz: “Prva recenica. Ovo je druga recenica. Na kraju treca.”
# Izlaz: PON


def task_61():
    string = input("Enter string: ")
    new_string = ""
    for i in string:
        if i.isupper():
            new_string += i
    print(new_string)


task_61()
