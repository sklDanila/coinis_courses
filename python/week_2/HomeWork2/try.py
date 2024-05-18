# Takmičari su radili testove iz matematike i programiranja. Za svaki predmet dobili su
# određeni broj poena (cio broj od 0 do 50). Takmičari se rangiraju po ukupnom broju
# poena iz oba predmeta. Ako dva takmičara imaju isti broj poena, pobjednik je onaj koji
# ima više poena iz programiranja. Potrebno je napisati program koji određuje pobjednika
# takmičenja.


def competitions():
    while True:
        num_of_participants = int(
            input("Enter the number of participants in the competition: ")
        )
        if num_of_participants > 0:
            points = []
            sum = 0
            for i in range(num_of_participants):
                while True:
                    points_m = int(
                        input(
                            f"Enter the number of math points for the {i+1} participant: "
                        )
                    )
                    points_p = int(
                        input(
                            f"Enter the number of programming points for the {i+1} participant: "
                        )
                    )
                    if 0 <= points_m <= 50 and 0 <= points_p <= 50:
                        points.append((points_m, points_p))
                        break
                    else:
                        print("You need to enter points from 0 to 50!")
            for i in range(len(points)):
                sum_points = points[i][0] + points[i][1]
                if sum_points > sum:
                    sum = sum_points

            print(sum)

            break


competitions()
