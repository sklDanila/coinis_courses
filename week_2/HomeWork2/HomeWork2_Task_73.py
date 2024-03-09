# Za RPG igru, napravi program koji simulira inventar igrača. Inventar može biti lista tkz.
# itema, odnosno predmeta (npr. mač, šešir, rukavice,...). Vaš zadatak je da na osnovu
# pozicije u inventaru otkrijete koji je to predmet (za pristup koristiti indeks liste)


def task_73():
    list = ["sword", "hat", "gloves"]
    num = int(input("Enter number of item: "))

    match num:
        case 0:
            print(list[0])
        case 1:
            print(list[1])
        case 2:
            print(list[2])


task_73()
