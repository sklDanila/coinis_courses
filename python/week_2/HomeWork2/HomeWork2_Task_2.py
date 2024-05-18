# U selu poznatom po svojim jabukama, održava se godišnje takmičenje u berbi jabuka
# između i najbliži pobjedi su Petar i Miloš. Petar tvrdi da je ubrao p jabuka, dok Miloš tvrdi
# da je ubrao m jabuka. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je Petar
# uspio da ubere više jabuka nego Miloš i shodno tome ispiše poruku o pobjedniku.
# Pretpostaviti da ne mogu ubrati isti broj jabuka.


def apples():
    while True:
        p = int(input("Enter the number of apples that Peter collected: "))
        m = int(input("Enter the number of apples that Milash collected: "))

        if p >= 0 and m >= 0:
            if p > m:
                print(f"Peter collected {p} apples and WON the competition.")
            elif p < m:
                print(f"Miloš collected {m} apples and WON the competition.")
            break
        else:
            print("Enter positive numbers!")


apples()
