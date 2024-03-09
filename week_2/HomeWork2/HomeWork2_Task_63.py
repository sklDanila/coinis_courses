# Za dati string koji sadrži praznine (blankove), odrediti najdužu riječ u stringu.


def task_63():
    string = input("Enter string: ")
    new_strings = string.split(" ")

    longest_word = ""
    for word in new_strings:
        if len(word) > len(longest_word):
            longest_word = word

    print(longest_word)


task_63()
