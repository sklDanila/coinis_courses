# Na takmičenju iz matematike učestvovalo je N učenika. Izveštaj o broju poena
# odštampan je na dvije strane. Nastavnik greškom nije ponio prvu stranu izveštaja, ali se
# sjeća da je na dnu strane pisalo da je prosječan broj poena za tu stranu bio p1. Na
# drugoj strani (koju ima kod sebe) su podaci o K učenika i prosječan broj poena za tu
# stranu je p2. Napisati program kojim se određuje koliki je prosječan broj poena svih
# učenika.
# Ulaz: Na standardnom ulazu nalaze se
# • u prvoj liniji prirodan broj N ukupna broj učenika
# • u drugoj liniji prirodan broj K broj učenika na drugoj strani
# • u trećoj liniji realan broj p1 prosječan broj poena učenika na prvoj strani
# • u četvrtoj liniji realan broj p2 prosječan broj poena učenika na drugoj strani
# Izlaz: Na standarnom izlazu prikazati, na dvije decimale, prosječan broj bodova svih
# učenika.
# Primjer
# Ulaz: 80, 30, 78.20, 89.30
# Izlaz: 82.36


def mathematics_exam():
    while True:
        N = int(input("Enter the total number of students: "))
        K = int(input("Enter the number of students on the second side: "))
        p1 = float(input("Enter the average number of points on first side: "))
        p2 = float(input("Enter the average number of points on second side: "))

        if N > 0 and K > 0 and p1 > 0 and p2 > 0:
            average_points = ((p2 * K) + (p1 * (N - K))) / N
            print(f"Average points are {round(average_points, 2)}")
            break
        else:
            print("Enter positive variables")


mathematics_exam()
