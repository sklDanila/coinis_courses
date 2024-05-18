# Napisati program koji skraćuje string do unijete dužine. Na kraj stringa dodati ... Ako je
# unijeza dužina veća od same dužine stringa, na kraju stringa dodati samo ...
# Primjer 1:
# string: “abcde”, duzina: 2, štampa se “ab...”
# Primjer 2:
# string: “abcde”, duzina: 10, štampa se “abcde...”
def task_49():
    string = str(input("Enter string: "))
    length = int(input("Length of the shortened string: "))

    if length > len(string):
        string += "..."
    elif length < len(string):
        string = string[:length] + "..."

    print(f"Shortened string is: {string}")


task_49()
