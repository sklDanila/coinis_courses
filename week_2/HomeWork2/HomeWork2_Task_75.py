# Napisati program koji izračunava ukupni gubitak banke za godinu dana od kamate na
# štednju. Korisnik unosi listu početnih iznosa štednje klijenata. Takođe, korisnik unosi
# fiksnu kamatnu stopu na štednju (za sve korisnike ista). Program izračunava i ispisuje
# ukupni gubitak banke od kamate nakon datog perioda.


def task_75():
    list = []
    for i in range(5):
        save = int(input(f"Enter attachment for {i+1} account: "))
        list.append(save)
    percent = int(input(f"Enter the fixed annual interest rate for all clients: "))

    sum = 0

    for i in list:
        sum += i / 100 * percent
    print("The bank's loss", sum)


task_75()
