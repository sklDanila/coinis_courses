# Neka je data lista artikala u jednoj prodavnici. Pronaći vrijednost drugog najskupljeg
# proizvoda u prodavnici.


def task_78():
    prices = [100, 300, 200, 5657, 5555]
    prices.sort()
    return prices[-2]


print(task_78())
