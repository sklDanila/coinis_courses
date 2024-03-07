# Ako tekst ima više od 30 karaktera skratiti ga tako da ostane tačno 30 karaktera, a na
# kraj skraćenog teksta dodati ...


def text():
    text = str(input("Enter the text: "))

    if len(text) > 30:
        text = text[:30]
        print(f"{text}...  Length is {len(text)}")


text()
