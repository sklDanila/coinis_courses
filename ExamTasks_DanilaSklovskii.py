import random

# Task 1a
# def povrsina(width, height):
#     povrsina = (width * height) / 10000
#     print(f"Povrsina u metrima je {povrsina} m2")


# povrsina(int(input("Unesite vas sirine: ")), int(input("Unesite vas visine: ")))


# Task 1b
# def broker(kapital, cijena_prije):
#     akciji = kapital / (cijena_prije + cijena_prije / 100 * 15)
#     print(f"Broker moze da kupiti {akciji}")


# broker(
#     int(input("Enter your kapital: ")),
#     int(input("Unesite cijene akcije prije povencanja: ")),
# )


# Task 2a
# def strings(stringa):
#     r = []
#     rijeci = stringa.split(" ")
#     for i in rijeci:
#         if (
#             i[0]
#             in [
#                 "a",
#                 "e",
#                 "i",
#                 "o",
#                 "u",
#                 "y",
#             ]
#             and len(i) == 5
#         ):
#             r.append(i)
#     print(r)

# strings("anasr sam htio kupiti kavu")


# Task 3
# def broker2(stringa):
#     Izlaz = 0
#     sell_buy = stringa.split(" ")
#     for sell in sell_buy:
#         if sell[0] == "S":
#             Izlaz += int(sell[1:])
#     for buy in sell_buy:
#         if buy[0] == "B":
#             Izlaz -= int(buy[1:])
#     print(Izlaz)


# broker2("S50 S40 B50 B100")


# Task 4
# def brojevi(string):
#     count = 0
#     numbers = string.split(" ")
#     for i in numbers:
#         if i[0:2] == "0x":
#             count += 1
#     print(count)


# brojevi("12 0x1A 0001 121 0x2")


# Task 5
# def matrica():
#     matrix = []
#     for i in range(4):
#         matrix.append([])
#         for j in range(4):
#             matrix[i].append(random.choice(range(1, 11)))
#             print(random.choice(range(1, 11)), end="\t")
#         print("\n")

#     MaxSum = 0
#     for i in range(4):
#         sum = 0
#         for j in range(4):
#             sum += matrix[j][i]
#         if MaxSum < sum:
#             MaxSum = sum
#     print(MaxSum)


# matrica()
