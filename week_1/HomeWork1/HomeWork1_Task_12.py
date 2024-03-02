# Kreirati algoritam koji računa koje godine je rođen Miloš ukoliko je poznato da danas ima
# N godina.

from datetime import date


def birthday():
    while True:
        N = int(input("Enter your age: "))
        if N > 0:
            today = date.today()
            print(today.year - N)
            break
        else:
            print("Please enter a positive age.")


birthday()
