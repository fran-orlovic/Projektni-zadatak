from zdravstvena import unos_zdravstvene


def unos_korisnika(index):

    korisnik = {}

    korisnik['ime'] = input(f"Unesite ime {index}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {index}. korisnika: ").capitalize()
    korisnik['telefon'] = int(input(f"Unesite telefon {index}. korisnika: "))
    korisnik['email'] = input(f"Unesite email {index}. korisnika: ").strip()
    korisnik['zdravstvena'] = unos_zdravstvene(index)

    return korisnik
