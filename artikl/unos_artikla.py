from utilities import unos_pozitivnog_realnog_broja
from .artikl import Artikl


def unos_artikla(index):

    naslov = input(f"Unesite naslov {index}. artikla: ").capitalize()
    opis = input(f"Unesite opis {index}. artikla: ").capitalize()
    cijena = unos_pozitivnog_realnog_broja(f"Unesite cijenu {index}. artikla: ")

    artikl = Artikl(naslov, opis, cijena)

    return artikl
