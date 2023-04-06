from artikl import unos_artikla


def unos_kategorije(index):

    kategorija = {}

    kategorija['naziv'] = input(f"Unesite naziv {index}. kategorije: ").capitalize()
    artikli = []
    # tu napraviti dobar handling
    for artikl in artikli:
        kategorija['artikl'] = artikli.append(unos_artikla(index))

    return kategorija
