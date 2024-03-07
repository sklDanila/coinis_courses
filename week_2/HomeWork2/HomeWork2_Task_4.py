# Kućni red zabranjuje pravljenje buke prije 6 časova, između 13 i 17 časova i nakon 22
# časa. Napiši program koji radnicima govori da li u nekom datom trenutku mogu da
# izvode bučnije radove.

import datetime


def work():
    while True:
        time_now = datetime.datetime.now()
        hours_now = time_now.hour
        print(hours_now)

        if 6 < hours_now < 13 or 17 < hours_now < 22:
            print("Radnik može da radi.")
        else:
            print("Radnik ne moze da radi sad")
        break


work()
