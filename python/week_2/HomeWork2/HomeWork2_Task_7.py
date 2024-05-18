# Takmičari su radili testove iz matematike i programiranja. Za svaki predmet dobili su
# određeni broj poena (cio broj od 0 do 50). Takmičari se rangiraju po ukupnom broju
# poena iz oba predmeta. Ako dva takmičara imaju isti broj poena, pobjednik je onaj koji
# ima više poena iz programiranja. Potrebno je napisati program koji određuje pobjednika
# takmičenja.


def competitions():
    while True:
        points_math_1 = int(
            input(
                "Enter the number of math points for the first participant(from 0 to 50): "
            )
        )
        points_inf_1 = int(
            input(
                "Enter the number of informatics points for the first participant(from 0 to 50): "
            )
        )
        points_math_2 = int(
            input(
                "Enter the number of math points for the second participant(from 0 to 50): "
            )
        )
        points_inf_2 = int(
            input(
                "Enter the number of informatics points for the second participant(from 0 to 50): "
            )
        )

        if (
            0 <= points_math_1 <= 50
            and 0 <= points_math_2 <= 50
            and 0 <= points_inf_1 <= 50
            and 0 <= points_inf_2 <= 50
        ):
            if points_math_1 + points_inf_1 > points_math_2 + points_inf_2:
                print("The winner is the first player.")
            elif points_math_1 + points_inf_1 == points_math_2 + points_inf_2:
                if points_inf_1 > points_inf_2:
                    print("The winner is the first player.")
                else:
                    print("The winner is the second player.")
            else:
                print("The winner is the second player.")
            break
        else:
            print("Enter points from 0 to 50!")


competitions()
