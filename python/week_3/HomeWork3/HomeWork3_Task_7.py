# Potrebno je implementirati jednostavnu biblioteku za upravljanje knjigama u programskom jeziku
# Python. Biblioteka treba omogućiti dodavanje, pregled, uređivanje i brisanje knjiga iz inventara.
# Potrebno je kreirati klasu Book i klasu Library.
# ● Svaka knjiga ima sledeće atribute: naslov, autor, godina izdanja i broj kopija u inventaru.
# ● Implementirati konstruktor klase Book koji će inicijalizovati atribute knjige. Implementirati
# metode za dohvatanje i postavljanje svakog atributa knjige (geteri i seteri).
# ● Biblioteka (Library) treba da sadrži listu knjiga koje su dostupne u inventaru.
# Implementirati metode za dodavanje knjige u inventar (Book objekat), brisanje knjige iz
# inventara (po naslovu), pretragu knjiga po naslovu ili autoru i prikaz svih knjiga koje su
# trenutno dostupne (naslov, autor i godina izdanja).
# ● Napisati glavni program koji koristi klasu Library za upravljanje inventarom knjiga.
# Korisnik treba da može da izabere opcije za dodavanje, pregled, uređivanje i brisanje
# knjiga iz biblioteke. Prilikom dodavanja knjige, program treba da omogući unos svih
# potrebnih informacija o knjizi. Prilikom uređivanja knjige, korisnik treba da može da
# izmeni bilo koji atribut knjige (naslov, autor, godina izdanja, broj kopija). Prilikom brisanja
# knjige, program treba da ukloni knjigu iz inventara na osnovu naslova knjige. Prilikom
# pretrage po naslovu ili autoru, program treba da prikaže sve knjige koje zadovoljavaju
# kriterijum pretrage.


class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_copies(self):
        return self.copies

    def set_copies(self, copy):
        self.copies = copy


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Invalid object!")

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                break

    def find_book_title(self, title):
        found_books = []
        for book in self.books:
            if title in book.get_title():
                found_books.append(book)
        return found_books

    def find_book_author(self, author):
        found_books = []
        for book in self.books:
            if author in book.get_author():
                found_books.append(book)
        return found_books

    def show_available_books(self):
        for book in self.books:
            print(
                f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nYear: {book.get_year()}\nCopies: {book.get_copies()}\n"
            )


def main():
    myLibrary = Library()

    while True:
        print("1. Add a book")
        print("2. Remove a book by title")
        print("3. Find books by title")
        print("4. Find books by author")
        print("5. Display available books")
        print("6. Quit")
        choice = int(input("Enter the action: "))

        match choice:
            case 1:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = input("Enter the year of publication: ")
                copies = int(input("Enter the number of copies: "))
                book = Book(title, author, year, copies)
                myLibrary.add_book(book)
                print("Book added successfully!\n")
            case 2:
                title = input("Enter title for removal: ")
                myLibrary.remove_book(title)
                print("\nBook removed successfully.\n")
            case 3:
                title = input("Enter title for search book: ")
                find_books = myLibrary.find_book_title(title)
                for book in find_books:
                    print(f"Title: {book.get_title()}\n")
            case 4:
                author = input("Enter author for search: ")
                find_authors = myLibrary.find_book_author(author)
                for book in find_authors:
                    print(f"Title: {book.get_title()}\n")
            case 5:
                myLibrary.show_available_books()
            case 6:
                break


main()
