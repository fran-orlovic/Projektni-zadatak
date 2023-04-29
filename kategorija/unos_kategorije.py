from artikl import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja
from .kategorija import Kategorija


def unos_kategorije(index):

    naziv = input(f"Unesite naziv {index}. kategorije: ").capitalize()
    broj_artikala = unos_pozitivnog_cijelog_broja(f"Unesite broj artikala za {index}. kategoriju: ")

    artikli = []
    for i in range(broj_artikala):
        artikli.append(unos_artikla(len(artikli) + 1))

    kategorija = Kategorija(naziv, artikli.copy())

    return kategorija
