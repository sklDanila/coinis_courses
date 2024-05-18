# def tdf():
#     v = 5
#     try:
#         print(v / 0)
#     except ZeroDivisionError as e:
#         print("Caught an exception:", type(e).__name__, ":", e.args)
#     finally:
#         print("Executing the 'finally' clause")


# tdf()
# print("\nDone!")


# def get_val():
#     while True:
#         try:
#             input_user = int(input("Enter number: "))
#         except Exception as e:
#             print("Error: ", type(e).__name__, e.args)
#         else:
#             print("Right. Its number")
#             break
#         finally:
#             print("Complited!")
#             print(input_user)


# get_val()

"""
Функционально программирование:
    1. Задавать переменные не внутри функции, а в аргументах функции
    2. Ипользовать рекурсию 
    3. Использовать генераторы (yield) - как обертку для итераторов
    4. Использовать копии, а не оригиналы данных
"""


# def square(a):
#     return a * a


# square_lambda = lambda a: a * a

# print(square(2))
# print(square_lambda(2))


# def build_quadratic(a, b, c):
#     return lambda x: a * x * x + b * x + c


# f = build_quadratic(2, 3, -5)
# print(f(0))
# print(f(1))
# print(f(2))


lista = [1, 3, 5, 6, 7, 8, 9, 10]
parni_elementi = filter(lambda x: x % 2 == 0, lista)
print(list(parni_elementi))


# city_temperature = [("Podgorica", 15), ("Niksic", 12), ("Tivat", 10)]

# city_temperature_fahrengent = map(
#     lambda city: (city[0], (9 / 5) * city[1] + 32), city_temperature
# )
# print(list(city_temperature_fahrengent))

# list_a = [10, 20, 30, 40]
# list_b = [20, 25, 10, 12]

# lista_c = map(lambda a, b: a + b, list_a, list_b)
# # print(list(lista_c))

# from functools import reduce

# sum = reduce(lambda x, y: x + y, lista_c)
# print(sum)
