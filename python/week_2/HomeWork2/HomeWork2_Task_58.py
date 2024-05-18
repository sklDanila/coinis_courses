# Napisati program koji od zadatog stringa kreira novi string koji se sastoji bez cifara.
# Primjer: “Hi Mr. Rober53. How are you today? Today is 08.10.2019”), vraća “Hi Mr.
# Rober. How are you today? Today is ..” kao string.
# Pomoć: da provjerite da li je karakter slovo koristiti isalpha metod, a da li je cifre koristite
# isdigit

import re


def task_58():
    string = input("Enter the string: ")
    new_string = re.sub("[0-9]", "", string)

    print(new_string)


task_58()
