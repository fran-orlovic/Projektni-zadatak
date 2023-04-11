from datetime import date


def unos_zdravstvene(index):

    zdravstvena = {}

    zdravstvena['oib'] = int(input(f"Unesite OIB {index}. korisnika: "))

    dan = int(input("Unesite dan izdavanja zdravstvene: "))
    mjesec = int(input("Unesite mjesec izdavanja zdravstvene: "))
    godina = int(input("Unesite godinu izdavanja zdravstvene: "))
    zdravstvena['datum_izdavanja'] = date(godina, mjesec, dan)

    return zdravstvena
