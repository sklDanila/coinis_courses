# Napisati program kojim se na osnovu datog prosjeka učenika prikazuje uspjeh učenika.
# Odličan uspjeh ima učenik čiji je prosjek veći ili jednak 4.5. Vrlodobar uspeh postiže
# učenik čiji je prosek veći ili jednak 3.5, a manji od 4.5, dobar uspeh se postiže za prosek
# koji je veći ili jednak 2.5 a manji od 3.5, dovoljan uspeh za prosek veći ili jednak 2, a
# manji od 2.5. Ako učenik ima neku jedinicu unijeće se prosjek 1, a uspeh mu je
# nedovoljan.


def grades():
    while True:
        count = int(input("Enter the number of student grades: "))
        sum = 0
        if count > 0:
            for i in range(count):
                while True:
                    grade = float(input(f"Enter the student's {i+1} grade: "))
                    if grade >= 0 and grade <= 5:
                        sum += grade
                        break
                    else:
                        print("Invalid mark! Please enter a value between 0 and 5.")
            avg = sum / count

            if avg >= 4.5:
                print("Excellent success!")
            elif 3.5 <= avg < 4.5:
                print("Very good success!")
            elif 2.5 <= avg < 3.5:
                print("Good success!")
            elif 2 <= avg < 2.5:
                print("Satisfactory success")
            else:
                print("Inadequate success")
            break


grades()
