# Napisati klasu Televizor koja se sastoji od sledećih atributa: broj tekućeg kanala (int, između 0 i
# dužine od liste kanala), naziv tekućeg kanala (string), kanali (lista stringova), jačina tona (int,
# između 0 i 10). Potrebno je odraditi sledeće:
# a. Napisati konstruktor kojim se postavljaju početne vrijednosti atributa. Za atribut kanali to
# treba da bude prazna lista.
# b. Kreirati odgovarajući getere i setere. Obratiti pažnju na ograničenja za attribute broj
# kanala i jačina tona.
# c. Napisati funkciju dodaj_kanal sa parametrom naziv kanala, koja dodaje novi kanal u listu
# kanala.
# d. Napisati funkciju obriši_kanal sa parametrom na naziv kanala, kojom se briše kanal na
# osnovu naziv.
# e. Napisati funkciju pojačaj_ton koja uvećava vrijednost tona za jedan u odnosu na
# trenutnu jačinu
# f. Napisati funkciju ime_kanala sa parametrom za broj kanala, koja vraća naziv kanala na
# osnosu zadatog broja.Prvi kanal se nalazi na poziciji 1


class TV:
    def __init__(self):
        self.number_of_channel = 0
        self.name_of_channel = ""
        self.channels = []
        self.ton = 0

    def set_number_of_channel(self, number):
        if 0 <= number < len(self.channels):
            self.number_of_channel = number
        else:
            print("Number is out of range channels")

    def set_name_of_channel(self, channel):
        self.name_of_channel = channel

    def set_ton(self, ton):
        if 0 <= ton <= 10:
            self.ton = ton
        else:
            print("Ton value must be between 0 and 10")

    def add_channel(self, name_of_channel):
        self.channels.append(name_of_channel)

    def delete_channel(self, name_of_channel):
        self.channels.remove(name_of_channel)

    def boost_tone(self):
        self.ton += 1

    def channel_name(self, number_of_channel):
        return self.channels[number_of_channel - 1]
