
def get_korisnik(index, korisnik):
    print(f"\t{index}. {korisnik.email} {korisnik.telefon}")


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()
