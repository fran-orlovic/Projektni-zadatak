from utilities import unos_pozitivnog_cijelog_broja, unos_emaila
from utilities import unos_intervala
from .privatni_korisnik import PrivatniKorisnik
from .poslovni_korisnik import PoslovniKorisnik
from .tip_korisnika import TipKorisnika


def unos_korisnika(index):

    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {index}. korisnika:")
    email = unos_emaila(f"Unesite email {index}. korisnika: ")

    print("Tipovi korisnika:")
    for i, tip_korisnika in enumerate(TipKorisnika, start=1):
        print(f"\t{i}. {tip_korisnika.value}")

    odabir_tipa = unos_intervala(1, len(TipKorisnika))

    if odabir_tipa == 2:
        naziv = input(f"Unesite naziv {index}. korisnika: ").capitalize()
        web = input(f"Unesite web {index}. korisnika: ")
        korisnik = PoslovniKorisnik(telefon, email, naziv, web)
    else:
        ime = input(f"Unesite ime {index}. korisnika: ").capitalize()
        prezime = input(f"Unesite prezime {index}. korisnika: ").capitalize()
        korisnik = PrivatniKorisnik(telefon, email, ime, prezime)

    return korisnik
