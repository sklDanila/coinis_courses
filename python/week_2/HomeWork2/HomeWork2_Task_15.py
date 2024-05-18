# Napisati kod koji za datu godinu određuje da li je prestupna i štampa odgovarajuću
# poruku.


def leap_year():
    year = int(input("Enter the year: "))

    if year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")


leap_year()
