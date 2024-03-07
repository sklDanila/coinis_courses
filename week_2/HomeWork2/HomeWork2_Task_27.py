# Napisati program kojim provjeravati da li String sadrži bar jedan samoglasnik.


def vowels():
    word = str(input("Enter sentence: "))

    counter = 0

    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u", "y"]:
            counter += 1

    if counter > 0:
        print("The string contains at least one vowel.")


vowels()
