# Napisati program koji račun X**n koristeći petlju (bez ugrađenog Python operatora za
# stepenovanje)
def exponent():
    X = int(input("Enter number: "))
    n = int(input("Enter exponent: "))
    result = 1
    for i in range(n):
        result *= X

    print(result)


exponent()
