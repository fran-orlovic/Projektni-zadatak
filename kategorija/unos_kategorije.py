from artikl import unos_artikla


def unos_kategorije(index):

    kategorija = {}

    kategorija['naziv'] = input(f"Unesite naziv {index}. kategorije: ").capitalize()
    broj_artikala = int(input(f"Unesite broj artikala za {index}. kategoriju: "))
    artikli = []
    for i in range(broj_artikala):
        artikli.append(unos_artikla(i + 1))
    kategorija['artikli'] = artikli.copy()
    return kategorija
