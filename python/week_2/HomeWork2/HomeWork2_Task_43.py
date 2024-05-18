# Data je lista ocjena na predmetu likovno za sve učenike jednog odjeljenja osnovne
# škole. Ispostavilo se da nema učenika koji imaju ocjenu 1 i 2. Prebrojati koliko učenika
# ima ostale ocjene (za svaku ocjenu pojedinačno).


def task_43():
    grades = [3, 3, 4, 5, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4]

    count_5 = 0
    count_4 = 0
    count_3 = 0

    for i in grades:
        match i:
            case 5:
                count_5 += 1

            case 4:
                count_4 += 1

            case 3:
                count_3 += 1

    print(f"5: {count_5}\n4: {count_4}\n3: {count_3}")


task_43()
