# Dat je petocifreni prirodan broj koji predstavlja broj stambene jedinice u zgradi.
# Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi stambena
# jedinica. Poznato je da se to može otkriti kada se na vrijednost srednje cifre
# zadatog broja doda vrijednost poslednje cifre. Štampati taj zbir


def floor():
    while True:
        number_block = str(input("Enter five-digit number of block: "))

        if len(number_block) == 5:
            average_figure = int(number_block[len(number_block) // 2])
            last_figure = int(number_block[-1])
            floor = average_figure + last_figure
            print(f"The floor where the apartment is located is {floor}")
            break
        else:
            print("Wrong input! Please, enter exactly five digits.")


floor()
