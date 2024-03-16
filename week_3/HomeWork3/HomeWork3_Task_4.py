# Za zadati string napisati program kojim se provjerava koliko puta se u stringu dva susjedna
# karaktera ponavljaju (poklapaju).
# Primjer: aabaaac rezultat je 3.


def task_4():
    string = "aabaaac"
    count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
    print(count)


task_4()
