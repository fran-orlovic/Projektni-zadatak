from datetime import date
from korisnik import get_korisnik
from kategorija import get_kategorija
from artikl import get_artikl


def unos_prodaje(korisnici, kategorije, index):

    prodaja = {}

    dan = int(input(f"Unesite dan isteka {index}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {index}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {index}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {index}. prodaje")
    for i, korisnik in enumerate(korisnici, start=1):
        get_korisnik(i, korisnik)

    odabir_korisnika = int(input("Odabrani korisnik: "))
    prodaja['korisnik'] = korisnici[odabir_korisnika - 1]

    print(f"Odaberite kategoriju {index}. prodaje")
    for i, kategorija in enumerate(kategorije, start=1):
        get_kategorija(i, kategorija)

    odabir_kategorije = int(input("Odabrana kategorija: "))
    prodaja['kategorija'] = kategorije[odabir_kategorije - 1]

    print(f"Odaberite artikl {index}. prodaje")
    artikli = prodaja['kategorija']['artikli'].copy()

    for i, artikl in enumerate(artikli, start=1):
        get_artikl(i, artikl)

    odabir_artikla = int(input("Odabrani artikl: "))
    prodaja['artikl'] = artikli[odabir_artikla - 1]

    return prodaja
