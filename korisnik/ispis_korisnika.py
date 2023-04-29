
def get_korisnik(index, korisnik):
    print(f"\t{index}. {korisnik.ime} {korisnik.prezime}")


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()
