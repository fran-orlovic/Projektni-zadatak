from artikl import ispis_artikla


def get_kategorija(index, kategorija):
    print(f"\t{index}. {kategorija['naziv']}")


def ispis_svih_kategorija(kategorije):
    for i, kategorija in enumerate(kategorije, start=1):
        get_kategorija(i, kategorija)
        artikli = kategorija['artikli'].copy()
        for artikl in artikli:
            ispis_artikla(artikl)
