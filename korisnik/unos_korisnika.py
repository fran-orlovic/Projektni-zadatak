from utilities import unos_pozitivnog_cijelog_broja, unos_emaila
from .korisnik import Korisnik
from zdravstvena import unos_zdravstvene


def unos_korisnika(index):

    ime = input(f"Unesite ime {index}. korisnika: ").capitalize()
    prezime = input(f"Unesite prezime {index}. korisnika: ").capitalize()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {index}. korisnika:")
    email = unos_emaila(f"Unesite email {index}. korisnika: ")
    zdravstvena = unos_zdravstvene(index)

    korisnik = Korisnik(ime, prezime, email, telefon, zdravstvena)

    return korisnik
