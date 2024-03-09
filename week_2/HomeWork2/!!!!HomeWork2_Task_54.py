# Dat je string sastavljen od karaktera 0 i 1. Karakter 0 predstavlja slobodno polje, a 1
# predstavlja zauzeto polje. Vaš zadatak je da za zadatu poziciju u stringu provjerite da li
# su susjedna polja slobodna (lijevo i desno). Napomena: za prvo polje gledate same
# desno polje, za poslednje polje samo lijevo polje, a za ostala i lijevo i desno polje. Npr.
# ako je string 01010, a zadata pozicija 2 (indeksiranje kreće od nule), treba štampati 0 jer
# nema slobodnih polja.
def task_54():
    string = input("Enter the string: ")
    pos = int(input("Enter the position: "))
    
    if pos == 0:
        if int(string(pos+1)) == 0:
            print(0)
        elif int(string(pos+1)) == 1:
            print(1)
    elif pos