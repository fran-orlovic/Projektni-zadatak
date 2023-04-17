from korisnik import get_korisnik
from kategorija import get_kategorija
from artikl import get_artikl
from utilities import unos_datuma, unos_intervala


def unos_prodaje(korisnici, kategorije, index):

    prodaja = {}

    prodaja['datum'] = unos_datuma("Unesite datum.")

    print(f"Odaberite korisnika {index}. prodaje")
    for i, korisnik in enumerate(korisnici, start=1):
        get_korisnik(i, korisnik)

    odabir_korisnika = unos_intervala(1, len(korisnici))
    prodaja['korisnik'] = korisnici[odabir_korisnika - 1]

    print(f"Odaberite kategoriju {index}. prodaje")
    for i, kategorija in enumerate(kategorije, start=1):
        get_kategorija(i, kategorija)

    odabir_kategorije = unos_intervala(1, len(kategorije))
    prodaja['kategorija'] = kategorije[odabir_kategorije - 1]

    print(f"Odaberite artikl {index}. prodaje")
    artikli = prodaja['kategorija']['artikli'].copy()

    for i, artikl in enumerate(artikli, start=1):
        get_artikl(i, artikl)

    odabir_artikla = unos_intervala(1, len(artikli))
    prodaja['artikl'] = artikli[odabir_artikla - 1]

    return prodaja
