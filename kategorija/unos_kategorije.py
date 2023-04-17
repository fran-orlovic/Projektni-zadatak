from artikl import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja


def unos_kategorije(index):

    kategorija = {}

    kategorija['naziv'] = input(f"Unesite naziv {index}. kategorije: ").capitalize()
    broj_artikala = unos_pozitivnog_cijelog_broja(f"Unesite broj artikala za {index}. kategoriju: ")
    artikli = []
    for i in range(broj_artikala):
        artikli.append(unos_artikla(len(artikli) + 1))
    kategorija['artikli'] = artikli.copy()
    return kategorija
