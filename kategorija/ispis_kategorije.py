
def get_kategorija(index, kategorija):
    print(f"\t{index}. {kategorija.naziv}")


def ispis_svih_kategorija(kategorije):
    for i, kategorija in enumerate(kategorije, start=1):
        get_kategorija(i, kategorija)
        kategorija.ispis()
