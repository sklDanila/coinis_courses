# Napisati program koji provjerava da li se string završava sa target stringom.
# Primjer 1: string:“Abcd”, target: “cd”, štampa se “Da”
# Primjer 2: string: “www.google.com”, target: “me”, štampa se “Ne”


def target_string():
    string = str(input("Enter string: "))
    target = str(input("Target string: "))

    if string[-len(target) :] == target:
        print("Yes")
    else:
        print("No")


target_string()
