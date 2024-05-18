# Napisati program koji iz zadatog stringa izdvaja samo samoglasnike i vraća taj novi
# string.
def task_50():
    string = str(input("Enter the string: "))
    new_string = str()

    for i in string:
        if i.lower() in ["a", "e", "i", "o", "u", "y"]:
            new_string += i

    print(new_string)


task_50()
