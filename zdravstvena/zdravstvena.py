
class Zdravstvena:
    def __init__(self, oib, datum_izdavanja):
        self.__oib = oib
        self.__datum_izdavanja = datum_izdavanja

    def ispis(self):
        print("Datum izdavanja:")
        print(f"\tDan: {self.datum_izdavanja.day}")
        print(f"\tMjesec: {self.datum_izdavanja.month}")
        print(f"\tGodina: {self.datum_izdavanja.year}")
        print("---------------------")

    @property
    def oib(self):
        return self.__oib

    @oib.setter
    def oib(self, oib):
        self.__oib = oib

    @property
    def datum_izdavanja(self):
        return self.__datum_izdavanja

    @datum_izdavanja.setter
    def datum_izdavanja(self, datum_izdavanja):
        self.__datum_izdavanja = datum_izdavanja
