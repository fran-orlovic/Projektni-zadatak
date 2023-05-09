from datetime import date
from .zdravstvena import Zdravstvena


def unos_zdravstvene(index):

    oib = int(input(f"Unesite OIB {index}. korisnika: "))

    dan = int(input("Unesite dan izdavanja zdravstvene: "))
    mjesec = int(input("Unesite mjesec izdavanja zdravstvene: "))
    godina = int(input("Unesite godinu izdavanja zdravstvene: "))
    datum_izdavanja = date(godina, mjesec, dan)

    zdravstvena = Zdravstvena(oib, datum_izdavanja)

    return zdravstvena
