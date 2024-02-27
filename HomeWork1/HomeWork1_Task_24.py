# Za Milicu i Anu se čuva koliko puta su obišle teren u 40 minuta. Međutim,
# prilikom unosa podataka desila se zabuna, pa je u varijabli x sačuvana vrijednost
# koja je trebala biti sačuvana u varijabli y i obrnuto. Napisati kod koji mijenja
# mjesta vrijednostima u promjenljivim x i y. Npr. ako je x = 7 i y = 10, poslije
# izvršavanja koda treba da bude x=10 i y=7.


def variable_values():
    x = int(input("Enter variable values for x: "))
    y = int(input("Enter variable values for y: "))

    variables = []

    variables.append(x)
    variables.append(y)

    x = variables[1]
    y = variables[0]

    print("Variable x now has value ", x)
    print("Variable y now has value ", y)


variable_values()
