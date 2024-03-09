# Korisnik unosi tri broja. Naći minimum i maksimum među unijetim brojevima i rezultat
# prikazati korisniku.


def task_47():
    list = []
    for i in range(3):
        num = int(input("Unesite broj: "))
        list.append(num)

    print(f"Max: {max(list)}\nMin: {min(list)}")


task_47()
