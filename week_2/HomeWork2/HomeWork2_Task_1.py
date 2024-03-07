# U tajanstvenom svijetu postoji portal koji se otvara samo kada mu se date paran broj.
# Kao mladi čarobnjak na svom prvom zadatku, dobio si čarobni štapić koji može
# generisati brojeve. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je broj koji
# je čarobni štapić generisao paran. Ako jeste, algoritam treba da ispiše: "Portal se
# otvara!" Ako nije, algoritam treba da ispiše: "Portal ostaje zatvoren."

import random


def random_num():
    while True:
        num = random.randint(0, 100)
        print(f"The magic wand generated a number {num}")

        if num % 2 == 0:
            print("The portal is opening!")
            break
        else:
            print("The portal is closed.")


random_num()
