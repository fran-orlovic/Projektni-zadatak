

def ispis_korisnika(korisnik):
    print("Informacije o korisniku")
    print(f"\tIme: {korisnik['ime']}")
    print(f"\tPrezime: {korisnik['prezime']}")
    print(f"\tTelefon: {korisnik['telefon']}")
    print(f"\tEmail: {korisnik['email']}")


def get_korisnik(index, korisnik):
    print(f"\t{index}. {korisnik['ime']} {korisnik['prezime']}")


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        ispis_korisnika(korisnik)
