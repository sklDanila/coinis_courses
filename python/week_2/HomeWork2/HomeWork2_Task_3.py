# Zamislimo da pravimo program koji treba da odluči da li student može da pristupi ispitu.
# Postoje dva uslova: student mora imati više od 75% prisustva na predavanjima i mora
# imati predate sve seminarske radove. Oba uslova moraju biti zadovoljena da bi student
# mogao pristupiti ispitu. Algoritam treba da štampa odgovarajuću poruku. Dodatak:
# prisustvo se unosi u procentima, a dio za seminarske radove na sledeci nacin -> 0
# predstavlja da bar jedan seminarski rad nike uradjen, a 1 da su svi seminarski radovi
# uradjeni.


def exam():
    while True:
        visit = int(input("Enter the percentage of student lecture attendance: "))
        pass_seminars = int(
            input(
                "Enter 0 if at least one seminar work has not been completed, 1 if all seminar work has been completed: "
            )
        )

        if 0 <= visit <= 100 and (pass_seminars == 0 or pass_seminars == 1):
            if visit > 75 and pass_seminars == 1:
                print("The student can take the exam.")
            else:
                print("The student can't take the exam.")
            break
        else:
            print("Enter correct values!")


exam()
