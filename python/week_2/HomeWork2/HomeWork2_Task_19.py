# U jednoj privatnoj školi uvedeno je pravilo kojim se određuje iznos popusta koji ostvaruju
# učenici prilikom upisa u narednu školsku godinu. Učenici sa odličnim uspehom ostvaruju
# popust od 40% ukupnog iznosa školarine, sa vrlodobrim 20% a sa dobrim 10%. Takođe,
# učenici koji su osvojili nagradu na nekom od državnih takmičenja ostvaruju popust od
# 30% ukupnog iznosa školarine. Ukoliko neki učenik ispunjava dva kriterijuma za popust
# primenjuje se kriterijum po kome je popust veći. Na osnovu punog iznosa školarine,
# prosečne ocene učenika i informacije o nagradama sa takmičenja odrediti iznos koji
# učenik treba da plati pri upisu u narednu školsku godinu.
# Ulaz: U prvoj varijabli nalazi se pun iznos školarine (realan broj), u drugoj prosječna
# ocjena učenika (realan broj od 2.0 do 5.0) a u trećoj 0 ukoliko učenik nema nagradu ili 1
# ukoliko je ima.
# Izlaz: Iznos školarine koju učenik treba da plati (zaokružen na najbliži cio broj) navodi se
# u jednoj linije standardnog izlaza


def sale():
    price = int(
        input("Enter price of the student to purchase the school year ticket: ")
    )
    average_mark = float(
        input("Enter the average mark of the student(from 2.0 to 5.0): ")
    )
    has_award = int(input("Has the student won an award? Enter 0 if no and 1 if yes: "))

    if 4.5 < average_mark < 5.0:
        price = price * 0.6
        print(round(price))
    elif 4.0 < average_mark < 4.5:
        match has_award:
            case 0:
                price = price * 0.8
                print(round(price))
            case 1:
                price = price * 0.7
                print(round(price))
    elif 3.5 < average_mark < 4.0:
        match has_award:
            case 0:
                price = price * 0.9
                print(round(price))
            case 1:
                price = price * 0.7
                print(round(price))
    else:
        print(price)


sale()
