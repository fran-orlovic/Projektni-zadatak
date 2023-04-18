from utilities import unos_pozitivnog_cijelog_broja, unos_emaila


def unos_korisnika(index):

    korisnik = {}

    korisnik['ime'] = input(f"Unesite ime {index}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {index}. korisnika: ").capitalize()
    korisnik['telefon'] = unos_pozitivnog_cijelog_broja(f"Unesite telefon {index}. korisnika:")
    korisnik['email'] = unos_emaila(f"Unesite email {index}. korisnika: ")

    return korisnik
